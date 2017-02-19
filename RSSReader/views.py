from django.shortcuts import render

from RSSReader.models import Sitio, Entrada, Anuncio


def index(request):
    sitios = Sitio.objects.filter(activo=True).order_by('?')
    feeds = []
    for sitio in sitios:
        feeds.extend(Entrada.objects.filter(sitio=sitio).order_by('-timestamp')[:5])

    return render(request, 'index.html', {'sitios': sitios, 'feeds': feeds, 'anuncios': Anuncio.objects.all()})
