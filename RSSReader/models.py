from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from RSSReader.RSSFetch import get_feed_url, get_news


class Sitio(models.Model):
    url = models.TextField()
    titulo = models.CharField(max_length=250)
    foto = models.FileField(upload_to='.')
    activo = models.BooleanField(default=True)
    rss = models.TextField(null=True, blank=True)
    upsidedown = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Sitio)
def insertar_rss(sender, instance, created, **kwargs):
    if not instance.rss or instance.rss == '':
        instance.rss = get_feed_url(instance.url)
        instance.save()

    if instance.activo:
        scan(instance)

class Entrada(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    url = models.TextField()
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Anuncio(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return self.titulo + ": " + self.texto


def scan(sitio):
    aux = []
    for feed in get_news(sitio.rss):
        # print(feed)
        if len(Entrada.objects.filter(url=feed['url'])) == 0:
            if not sitio.upsidedown:
                Entrada(sitio=sitio, url=feed['url'], titulo=feed['titulo'], descripcion=feed['descripcion']).save()
            else:
                aux.append(Entrada(sitio=sitio, url=feed['url'], titulo=feed['titulo'], descripcion=feed['descripcion']))

    for f in reversed(aux):
        f.save()