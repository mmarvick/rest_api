# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length='100')),
                ('phone', models.CharField(max_length='15')),
                ('address', models.CharField(max_length='200')),
                ('city', models.CharField(max_length='80')),
                ('stateProvince', models.CharField(max_length='80')),
                ('zip', models.CharField(max_length='10')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('happyHourStart', models.DateTimeField()),
                ('happyHourEnd', models.DateTimeField()),
                ('createdBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='restaurants')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
