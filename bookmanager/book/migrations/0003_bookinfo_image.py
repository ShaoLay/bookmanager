# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190415_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='book', verbose_name='图片'),
        ),
    ]