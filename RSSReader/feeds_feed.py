# coding=utf-8
# -*- coding: UTF-8 -*-
from django.contrib.syndication.views import Feed

from RSSReader.models import Entrada


class LatestFeedsFeed(Feed):
    title = "Últimas noticias"
    link = ""
    description = "Últimas noticias encontradas"

    def items(self):
        return Entrada.objects.order_by('-timestamp')[:15]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return item.url