# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('original_word', models.CharField(max_length=255)),
                ('type', models.PositiveIntegerField(choices=[(1, b'isim'), (2, b'eylem'), (3, b's\xc4\xb1fat'), (4, b'zamir')])),
                ('origin', models.ForeignKey(to='base.Origin')),
                ('related_words', models.ManyToManyField(related_name='related_words_rel_+', to='base.Word', blank=True)),
            ],
        ),
    ]
