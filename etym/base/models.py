from django.db import models
from django.utils.encoding import smart_unicode

from .constants import WORD_TYPES


class Origin(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8)

    def __unicode__(self):
        return smart_unicode(self.name)


class Word(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=255)
    origin = models.ForeignKey(Origin)
    original_word = models.CharField(max_length=255)
    type = models.PositiveIntegerField(choices=WORD_TYPES)
    related_words = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)

