import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotiWeb.settings')
import django

django.setup()

from RSSReader.models import Sitio, scan

if __name__ == '__main__':
    for sitio in Sitio.objects.all():
        scan(sitio)
