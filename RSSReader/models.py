from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from RSSReader.RSSFetch import get_feed_url, get_news


class Sitio(models.Model):
    url = models.CharField(max_length=1000, unique= True)
    titulo = models.CharField(max_length=250)
    foto = models.FileField(upload_to='.')
    activo = models.BooleanField(default=True)
    rss = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Sitio)
def insertar_rss(sender, instance, created, **kwargs):
    if created:
        if not instance.rss or instance.rss == '':
            instance.rss = get_feed_url(instance.url)
            instance.save()

        scan(instance)



class Entrada(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, unique=True)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Anuncio(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo+": "+self.texto



def scan(sitio):
    feed_url = get_feed_url(sitio.url)
    print(feed_url)

    for feed in get_news(sitio.rss):
        print(feed)
        if len(Entrada.objects.filter(url=feed['url'])) == 0:
            Entrada(sitio=sitio, url=feed['url'], titulo=feed['titulo'], descripcion=feed['descripcion']).save()