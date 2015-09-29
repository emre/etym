from django_redis import get_redis_connection
from django.core import cache

from models import Word
from constants import WORD_ID_SET_KEY


def get_random_word_id(r):
    return r.srandmember(WORD_ID_SET_KEY)


def create_word_id_list(r):
    r.sadd(
        WORD_ID_SET_KEY,
        *Word.objects.all().values_list('id', flat=True)
    )


def revalidate_id_list(r):
    r.delete(WORD_ID_SET_KEY)

    create_word_id_list(r)


def revalidate_and_get_random(r):
    revalidate_id_list(r)
    random_word_id = get_random_word_id(r)

    if not random_word_id:
        raise ValueError("no entries")

    return random_word_id


def get_random_word():
    r = get_redis_connection()

    random_word_id =  get_random_word_id(r)
    if not random_word_id:
        random_word_id = revalidate_and_get_random(r)

    return Word.objects.get(pk=random_word_id)
