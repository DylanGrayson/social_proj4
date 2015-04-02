# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_post_api_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='api_datetime',
        ),
    ]
