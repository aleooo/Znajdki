from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserRegistrationForm, RzeczyForm, MapaForm
from .models import Category, Rzeczy, Mapa


def start(request):
    return render(request, 'main/lista.html')


def objects_list(request, category_slug=None, sort=None):
    categories = Category.objects.all()
    kat = False
    monety = False
    objects = Rzeczy.objects.filter(user=request.user)
    recently = Rzeczy.objects.order_by('-publish')[:5]

    page = request.GET.get('page')
    sort = request.GET.get('sort')

    maps = [r.location for r in objects]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        objects = Rzeczy.objects.filter(category=category, user=request.user)
        maps = [r.location for r in objects]
        kat = True

    if sort:
        objects = objects.order_by(sort)

    paginator = Paginator(objects, 12)
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
                                               'maps': maps,
                                               'page': page,
                                               'recently': recently
                                               })


@login_required
def object_detail(request, *args, **kwargs):
    object = Rzeczy.objects.get(pk=kwargs['id'])
    maps = object.location
    form = RzeczyForm(instance=object)
    return render(request, 'main/detail.html', {'form': form,
                                                'maps': maps,
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
    type_side = 'create'

    create_form = RzeczyForm(request.POST or None, request.FILES or None)
    mapa_form = MapaForm(request.POST or None)
    if create_form.is_valid() and mapa_form.is_valid():
        opis = create_form.cleaned_data
        new_map = mapa_form.save(commit=False)
        new_map.description = opis['name']
        new_item = create_form.save(commit=False)
        mapa = mapa_form.save()
        new_item.slug = slugify(new_item.name)
        new_item.user = request.user
        new_item.location = mapa
        new_item.save()
    return render(request, 'main/create.html', {'form': create_form,
                                                'mapa_form': mapa_form,
                                                'type': type_side
                                                })

def search(request):
    print('Works')
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

    form = RzeczyForm(request.POST or None, request.FILES or None, instance=object)
    mapa_form = MapaForm(request.POST or None, instance=object.location)
    if form.is_valid() and mapa_form.is_valid():
        data = form.cleaned_data
        update_map = mapa_form.save(commit=False)
        update_map.description = data['name']
        update_map.save()
        main = form.save(commit=False)
        main.slug = slugify(data['name'])
        main.user = request.user
        main.location = update_map
        main.save()
        return redirect('poszukiwania:objects_list')
    return render(request, 'main/create.html', {'form': form,
                                                'mapa_form': mapa_form,
                                                'type': type_side
                                                })



