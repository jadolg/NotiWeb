# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSSReader', '0002_auto_20170217_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000, unique=True)),
            ],
        ),
    ]