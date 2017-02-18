FROM ubuntu:16.04

MAINTAINER Akiel <diazorozcoj@gmail.com>

LABEL version='1.0'
LABEL description='Django_NotiWeb'

RUN apt install python3 python3-pip gunicorn3 python3-gevent python3-mysqldb -y
ADD libs /home/libs
ADD requirements.txt /home

RUN pip3 install --no-index --find-links="/home/libs" -r /home/requirements.txt
WORKDIR /home/NotiWeb

ENTRYPOINT ["/usr/bin/python3"]
