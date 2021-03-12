from django.shortcuts import render
from .models import Kategoria, Rzeczy
from django.shortcuts import get_object_or_404


def rzeczy_list(request, kategoria_slug=None):
    categories = Kategoria.objects.all()
    rzeczy = Rzeczy.objects.all()
    maps = []
    kat = False
    monety = False
    if kategoria_slug:
   #     category = Kategoria.objects.filter(slug=kategoria_slug)
        category = get_object_or_404(Kategoria, slug=kategoria_slug)
        rzeczy = Rzeczy.objects.filter(kategoria=category)
        kat = True
        maps = [r.location for r in rzeczy]
        
    return render(request, 'main/lista.html', {'rzeczy': rzeczy,
                                               'categories': categories,
                                               'monety': monety,
                                               'kat': kat,
                                               'maps': maps,
                                               })


def rzecz_detail(request, year, month, day, rzecz_slug, id):
    rzecz = get_object_or_404(Rzeczy, pk=id)
    maps = rzecz.location
    return render(request, 'main/detail.html', {'rzecz': rzecz,
                                                'maps': maps,})
