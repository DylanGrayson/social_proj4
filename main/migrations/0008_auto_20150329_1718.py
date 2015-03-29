# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_corgi_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corgi',
            name='image',
            field=models.ImageField(default=b'../../static/profile_images/no_image.png', upload_to=b'../../static/profile_images/'),
            preserve_default=True,
        ),
    ]
