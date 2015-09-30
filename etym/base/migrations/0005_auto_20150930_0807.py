# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150930_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
