from django.db import models
from django.utils.encoding import smart_unicode
from django.db.models.signals import (post_save, pre_save)
from django.dispatch import receiver
from django.shortcuts import redirect

from django_redis import get_redis_connection
from unicode_tr.extras import slugify

from .constants import WORD_TYPES


class Origin(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8)

    def __unicode__(self):
        return smart_unicode(self.name)


class Word(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)
    origin = models.ForeignKey(Origin)
    original_word = models.CharField(max_length=255)
    type = models.PositiveIntegerField(choices=WORD_TYPES)
    derived_words = models.ManyToManyField("self", blank=True)
    root_word = models.ForeignKey("self", blank=True, null=True)
    is_active = models.BooleanField(default=False)

    @property
    def word_type(self):
        return dict(WORD_TYPES)[self.type]

    def __unicode__(self):
        return smart_unicode(self.name)


@receiver(pre_save, sender=Word)
def prepare_slug_handler(sender, **kwargs):
    instance = kwargs.get("instance")

    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()


@receiver(post_save, sender=Word)
def revalidate_cache_handler(sender, **kwargs):
    # inline import to prevent circular import error.
    from .utils import revalidate_id_list
    revalidate_id_list(get_redis_connection())
