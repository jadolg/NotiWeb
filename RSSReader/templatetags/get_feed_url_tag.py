from datetime import date
from django import template

from RSSReader.RSSFetch import get_feed_url

register = template.Library()


@register.simple_tag
def feed_url(url):
    return get_feed_url(url)