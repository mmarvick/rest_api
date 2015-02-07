# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=b'80')),
                ('phone', models.CharField(max_length=b'15')),
                ('address', models.CharField(max_length=b'200')),
                ('city', models.CharField(max_length=b'80')),
                ('stateProvince', models.CharField(max_length=b'80')),
                ('zip', models.CharField(max_length=b'10')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('happyHourStart', models.DateTimeField()),
                ('happyHourEnd', models.DateTimeField()),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
