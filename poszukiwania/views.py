from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserRegistrationForm, RzeczyForm, MapaForm
from .models import Kategoria, Rzeczy, Mapa


def start(request):
    return render(request, 'main/lista.html')


def rzeczy_list(request, kategoria_slug=None, sort=None):
    categories = Kategoria.objects.all()
    rzeczy = Rzeczy.objects.filter(user=request.user)

    maps = []
    kat = False
    monety = False

    if kategoria_slug:
        # category = get_object_or_404(Kategoria, slug=kategoria_slug)
        category = Kategoria.objects.get(slug=kategoria_slug)
        rzeczy = Rzeczy.objects.filter(kategoria=category, user=request.user)
        kat = True
        # maps = [r.location for r in rzeczy]
        maps = Mapa.objects.all()


    sort = request.GET.get('sort')
    if sort:
        rzeczy = rzeczy.order_by(sort)

    paginator = Paginator(rzeczy, 12)
    page = request.GET.get('page')
    try:
        obiekty = paginator.page(page)
    except PageNotAnInteger:
        obiekty = paginator.page(1)
    except EmptyPage:
        obiekty = paginator.page(paginator.num_pages)
    return render(request, 'main/lista.html', {'rzeczy': obiekty,
                                               'categories': categories,
                                               'monety': monety,
                                               'kat': kat,
                                               'maps': maps,
                                               'page': page,
                                               })


@login_required
def rzecz_detail(request, year, month, day, rzecz_slug, id):
    rzecz = Rzeczy.objects.get(pk=id)
    maps = rzecz.location
    return render(request, 'main/detail.html', {'rzecz': rzecz,
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
    print('Działa')
    if request.is_ajax():
        znajdka = request.POST.get('znajdka')
        lista = Rzeczy.objects.filter(title__icontains=znajdka)
        if len(lista) > 0 and len(znajdka) > 0:
            data = []
            for rzecz in lista:
                item = {
                    'pk': rzecz.pk,
                    'title': rzecz.title,
                    'image': str(rzecz.image.url),
                    'publish': rzecz.publish
                }
                data.append(item)
            list = data
        else:
            list = 'Brak obiektów'
        return JsonResponse({'data': list})
    return JsonResponse({})





