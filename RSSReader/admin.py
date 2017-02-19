from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from RSSReader.models import Sitio, Entrada, Anuncio

admin.site.unregister(Group)

class SitioAdmin(admin.ModelAdmin):
    def desactivar(modeladmin, request, queryset):
        for sitio in queryset:
            sitio.activo = False
            sitio.save()

    def activar(modeladmin, request, queryset):
        for sitio in queryset:
            sitio.activo = True
            sitio.save()

    def reiniciar(modeladmin, request, queryset):
        for sitio in queryset:
            for entrada in Entrada.objects.filter(sitio=sitio):
                entrada.delete()

            sitio.activo = True
            sitio.save()

    actions = [desactivar, activar, reiniciar,]


admin.site.register(Sitio, SitioAdmin)
admin.site.register(Entrada)
admin.site.register(Anuncio)