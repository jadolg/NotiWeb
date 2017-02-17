from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from RSSReader.models import Sitio, Entrada, Anuncio

admin.site.unregister(Group)

admin.site.register(Sitio)
admin.site.register(Entrada)
admin.site.register(Anuncio)