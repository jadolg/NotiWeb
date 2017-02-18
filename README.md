# RSS Agregator for SNET

## Run with gunicorn3 + gevent
`gunicorn3 NotiWeb.wsgi:application --bind 0.0.0.0:8383 -k gevent -w 5`

## Docker

### Running on Docker
 1. Run a MySQL container:
 `docker run --name mysql_notiweb -e MYSQL_DATABASE=notiweb -e MYSQL_ROOT_PASSWORD=qweqwe123 -d mysql:5.6`

 2. Run Migrations
`docker run -v /home/akiel/PycharmProjects/NotiWeb/:/home/NotiWeb -p 8080:8000 --rm --link mysql_notiweb -it notiweb manage.py migrate`

 3. Create a superuser
 `docker run -v /home/akiel/PycharmProjects/NotiWeb/:/home/NotiWeb -p 8080:8000 --rm link mysql_notiweb -it notiweb manage.py createsuperuser`

 4. Start the updater process
 `docker run -v /home/akiel/PycharmProjects/NotiWeb/:/home/NotiWeb -p 8080:8000 --link mysql_notiweb -d notiweb scan_sites.py`

 5. Start the server

    - Run with gunicorn3 + gevent on Docker
        `docker run -v /home/akiel/PycharmProjects/NotiWeb/:/home/NotiWeb -p 8080:8000 --rm --link mysql_notiweb -d notiweb /usr/bin/gunicorn3 NotiWeb.wsgi:application --bind 0.0.0.0:8000 -k gevent -w 5`

    - Run development server on Docker
        `docker run -v /home/akiel/PycharmProjects/NotiWeb/:/home/NotiWeb -p 8080:8000 --rm --link mysql_notiweb -it notiweb manage.py runserver 0.0.0.0:8000`