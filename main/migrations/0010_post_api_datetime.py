# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150329_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='api_datetime',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
