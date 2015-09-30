# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_word_root_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='related_words',
        ),
        migrations.AddField(
            model_name='word',
            name='derived_words',
            field=models.ManyToManyField(related_name='derived_words_rel_+', to='base.Word', blank=True),
        ),
    ]
