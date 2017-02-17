# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000, unique=True)),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000, unique=True)),
                ('titulo', models.CharField(max_length=250)),
                ('foto', models.FileField(upload_to='.')),
                ('activo', models.BooleanField(default=True)),
                ('rss', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='sitio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSSReader.Sitio'),
        ),
    ]