# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='root_word',
            field=models.ForeignKey(blank=True, to='base.Word', null=True),
        ),
    ]
