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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('createdBy', models.ForeignKey(related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
