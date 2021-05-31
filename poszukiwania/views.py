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
    objects = Rzeczy.objects.filter(user=request.user)

    maps = []
    kat = False
    monety = False

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        #category = Category.objects.get(slug=category_slug)
        objects = Rzeczy.objects.filter(category=category, user=request.user)
        kat = True
        maps = [r.location for r in objects]
        # maps = Mapa.objects.all()


    sort = request.GET.get('sort')
    if sort:
        objects = objects.order_by(sort)

    paginator = Paginator(objects, 12)
    page = request.GET.get('page')
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
                                               })


@login_required
def object_detail(request, year, month, day, object_slug, id):
    object = Rzeczy.objects.get(pk=id)
    maps = object.location
    return render(request, 'main/detail.html', {'object': object,
                                                'maps': maps})


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
    if request.method == 'POST':
        create_form = RzeczyForm(request.POST, request.FILES)
        mapa_form = MapaForm(request.POST)
        if create_form.is_valid() and mapa_form.is_valid():
            opis = create_form.cleaned_data
            new_map = mapa_form.save(commit=False)
            new_map.description = opis['title']
            new_item = create_form.save(commit=False)
            mapa = mapa_form.save()
            new_item.slug = slugify(new_item.title)
            new_item.user = request.user
            new_item.location = mapa
            new_item.save()
    else:
        create_form = RzeczyForm()
        mapa_form = MapaForm()

    return render(request, 'main/create.html', {'create_form': create_form,
                                                'point': mapa_form
                                                })

def search(request):
    print('Works')
    if request.is_ajax():
        znajdka = request.POST.get('znajdka')
        objects = Rzeczy.objects.filter(title__icontains=znajdka)
        if len(objects) > 0 and len(znajdka) > 0:
            data = []
            for object in objects:
                item = {
                    'pk': object.pk,
                    'title': object.title,
                    'image': str(object.image.url),
                    'publish': object.publish
                }
                data.append(item)
            list = data
        else:
            list = 'no objects'
        return JsonResponse({'data': list})
    return JsonResponse({})





