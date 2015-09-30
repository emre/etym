# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150930_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='slug',
            field=models.SlugField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.PositiveIntegerField(choices=[(1, b'\xc4\xb0sim'), (2, b'Eylem'), (3, b'S\xc4\xb1fat'), (4, b'Zamir')]),
        ),
    ]
