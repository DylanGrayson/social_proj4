# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_corgi_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='corgi',
            name='owner',
            field=models.ForeignKey(default=8, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
