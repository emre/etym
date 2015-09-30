# -*- coding: utf-8 -*-

from rest_framework import routers, serializers, viewsets

from .models import Word, Origin


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin


class WordSerializerAsForeignKey(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ("root_word", "derived_words")


class WordSerializer(serializers.ModelSerializer):
    origin = OriginSerializer()
    root_word = serializers.StringRelatedField(read_only=True)
    derived_words = serializers.StringRelatedField(many=True)

    class Meta:
        model = Word


