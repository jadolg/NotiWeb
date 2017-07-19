from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render

from RSSReader.models import Sitio, Entrada, Anuncio, scan


def index(request):
    sitios = Sitio.objects.filter(activo=True).order_by('?')
    feeds = []
    for sitio in sitios:
        feeds.extend(Entrada.objects.filter(sitio=sitio).order_by('-timestamp')[:5])

    return render(request, 'index.html', {'sitios': sitios, 'feeds': feeds, 'anuncios': Anuncio.objects.all()})


def create_admin(request):
    admin = User(username='admin', email='diazorozcoj@gmail.com')
    admin.set_password('changeit')
    admin.save()

    return HttpResponse('OK')


def update_feeds(request):
    for sitio in Sitio.objects.filter(activo=True):
        try:
            scan(sitio)
        except:
            pass