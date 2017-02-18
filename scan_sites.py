import os
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotiWeb.settings')
import django

django.setup()

from RSSReader.models import Sitio, scan

if __name__ == '__main__':
    while 1:
        try:
            print('actualizando feeds...')
            for sitio in Sitio.objects.all():
                try:
                    scan(sitio)
                except:
                    pass
        except KeyboardInterrupt:
            break
        print('[] hecho. durmiendo ahora!')
        sleep(300)

