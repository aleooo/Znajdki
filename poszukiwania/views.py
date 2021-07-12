from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from importlib import import_module
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import translation
from django.utils.text import slugify


from .forms import UserRegistrationForm, RzeczyForm, MapForm
from .models import Category, Rzeczy


def style(request, *args, **kwargs):
    if request.is_ajax():
        type = request.POST.get('type')
        print(type)
        request.session['style'] = type
        return JsonResponse({})


@login_required()
def objects_list(request, category_slug=None, session=1):

    if session:
        request.session.setdefault('style', 'thumbnail')

    print(request.body)
    kat = False
    monety = False

    categories = Category.objects.all()
    objects = Rzeczy.objects.filter(user=request.user)
    recently = Rzeczy.objects.order_by('-publish')[:5]

    sort = request.GET.get('sort')

    maps = [r.location for r in objects]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        objects = Rzeczy.objects.filter(category=category, user=request.user)
        maps = [r.location for r in objects]
        kat = True

    if sort:
        objects = objects.order_by(sort)
        if sort == 'catalog_number':
            objects = Rzeczy.objects.filter(catalog_number__gt=0).order_by(sort)

    page = request.GET.get('page')
    paginator = Paginator(objects, 20)


    try:
        objects_pagination = paginator.page(page)
    except PageNotAnInteger:
        objects_pagination = paginator.page(1)
    except EmptyPage:
        objects_pagination = paginator.page(paginator.num_pages)
    return render(request, 'main/lista.html', {'objects': objects_pagination,
                                               'categories': categories,
                                               'monety': monety,
                                               'kat': kat,
                                               'page': page,
                                               'recently': recently,
                                               'maps': maps
                                               })


@login_required
def object_detail(request, *args, **kwargs):
    object = Rzeczy.objects.get(pk=kwargs['id'])
    point = object.location
    form = RzeczyForm(instance=object)
    return render(request, 'main/detail.html', {'form': form,
                                                'point': point,
                                                'object': object,
                                                })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('poszukiwania:login')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'main/register.html', {'user_form': user_form, })


@login_required
def create(request):
    work = None
    type_side = 'create'
    create_form = RzeczyForm(request.POST or None, request.FILES or None)
    map_form = MapForm(request.POST or None)
    if create_form.is_valid() and map_form.is_valid():
        opis = create_form.cleaned_data['name']
        new_map = map_form.save(commit=False)
        new_map.description = opis
        new_map.save()
        new_item = create_form.save(commit=False)
        new_item.location = new_map
        new_item.slug = slugify(new_item.name)
        new_item.user = request.user
        new_item.save()
        work = 1
    return render(request, 'main/create.html', {'form': create_form,
                                                'map': map_form,
                                                'type': type_side,
                                                'work': work
                                                })

def search(request):
    if request.is_ajax():
        znajdka = request.POST.get('znajdka')
        objects = Rzeczy.objects.filter(name__icontains=znajdka)
        if len(objects) > 0 and len(znajdka) > 0:
            data = []
            for object in objects:
                item = {
                    'pk': object.pk,
                    'name': object.name,
                    'image_obverse': str(object.image_obverse.url),
                    'image_reverse': str(object.image_reverse.url),
                    'publish': object.publish,
                    'url': object.get_absolute_url()
                }
                data.append(item)
            list = data
        else:
            list = 'no objects'
        return JsonResponse({'data': list})
    return JsonResponse({})


def update(request, *args, **kwargs):
    object = Rzeczy.objects.get(pk=kwargs['id'])
    type_side = 'update'
    point = object.location
    form = RzeczyForm(request.POST or None, request.FILES or None, instance=object)
    map_form = MapForm(request.POST or None, instance=object.location)
    if form.is_valid() and map_form.is_valid():
        data = form.cleaned_data
        update_map = map_form.save(commit=False)
        update_map.description = data['name']
        update_map.save()
        main = form.save(commit=False)
        main.location = update_map
        main.slug = slugify(data['name'])
        main.user = request.user
        main.save()
        return redirect('poszukiwania:objects_list')
    return render(request, 'main/create.html', {'form': form,
                                                'map': map_form,
                                                'point': point,
                                                'type': type_side
                                                })


def delete_objects(request, **kwargs):
    Rzeczy.objects.get(pk=kwargs['id']).delete()
    return redirect('poszukiwania:objects_list')

