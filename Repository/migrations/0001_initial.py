# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadedfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=50, null=True, blank=True)),
                ('file_size', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'UploadedFile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UploadData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_data', models.FileField(upload_to='')),
            ],
        ),
    ]
