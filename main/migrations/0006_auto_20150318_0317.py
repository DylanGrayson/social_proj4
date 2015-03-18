# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20150318_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recipient',
            field=models.ForeignKey(related_name='recipient_set', default=8, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(related_name='author_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
