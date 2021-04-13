from django.shortcuts import render
from .models import Kategoria, Rzeczy, Mapa
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, RzeczyForm, MapaForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils.text import slugify



def start(request):
    return render(request, 'main/lista.html')


def rzeczy_list(request, kategoria_slug=None):
    categories = Kategoria.objects.all()
    rzeczy = Rzeczy.objects.filter(user=request.user)
    maps = []
    kat = False
    monety = False
    if kategoria_slug:
        category = get_object_or_404(Kategoria, slug=kategoria_slug)
        rzeczy = Rzeczy.objects.filter(kategoria=category, user=request.user)
        kat = True
        maps = [r.location for r in rzeczy]
        
    return render(request, 'main/lista.html', {'rzeczy': rzeczy,
                                               'categories': categories,
                                               'monety': monety,
                                               'kat': kat,
                                               'maps': maps,
                                               })


@login_required
def rzecz_detail(request, year, month, day, rzecz_slug, id):
    rzecz = get_object_or_404(Rzeczy, pk=id)
    maps = rzecz.location
    return render(request, 'main/detail.html', {'rzecz': rzecz,
                                                'maps': maps,})


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
def add_map(request):
    if request.method == 'POST':
        mapa_form = MapaForm(request.POST)
        if mapa_form.is_valid():
            new_map = mapa_form
            new_map.save()
            return redirect('poszukiwania:create')
    else:
        mapa_form = MapaForm
    return render(request, 'main/map.html', {'point': mapa_form})


@login_required
def create(request):
    if request.method == 'POST':
        create_form = RzeczyForm(request.POST, request.FILES)
        if create_form.is_valid():
            new_item = create_form.save(commit=False)
            new_item.slug = slugify(new_item.title)
            new_item.user = request.user
            new_item.save()
    else:
        create_form = RzeczyForm()
    return render(request, 'main/create.html', {'create_form': create_form,
                                                })

