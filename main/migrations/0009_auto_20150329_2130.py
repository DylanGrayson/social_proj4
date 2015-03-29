# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150329_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corgi',
            name='image',
            field=models.ImageField(default=b'profile_pictures/no_image.png', upload_to=b'profile_pictures/'),
            preserve_default=True,
        ),
    ]
