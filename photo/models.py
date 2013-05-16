# coding=utf-8
import os
from time import time
from hashlib import md5
from random import getrandbits
from django.db import models
from django.db.models.signals import pre_delete
from django.db.models.fields.files import FieldFile


def get_filename(instance, filename):
    return os.path.join("photo", "{hash}.{ext}".format(
        hash=md5(str(getrandbits(9999)) + str(time())).hexdigest(),
        ext=filename.split('.')[-1]))


def file_cleanup(sender, instance, *args, **kwargs):
    for field_name, _ in instance.__dict__.iteritems():
        field = getattr(instance, field_name)
        if issubclass(field.__class__, FieldFile) and field.name:
            field.delete(save=False)


class Photo(models.Model):
    title = models.CharField(verbose_name=u"Название фотографии", max_length=300)
    author = models.CharField(verbose_name=u"Авто фотографии", max_length=300)
    user_id = models.CharField(verbose_name=u"Идентификатор пользователя", max_length=32)
    photo = models.ImageField(verbose_name=u"Фотография", upload_to=get_filename)

    class Meta(object):
        verbose_name = u"Фотография"
        verbose_name_plural = u"Фотографии"

pre_delete.connect(file_cleanup, sender=Photo)


class Vote(models.Model):
    photo = models.ForeignKey(verbose_name=u"Фотография", to=Photo)
    user_id = models.CharField(verbose_name=u"Идентификатор пользователя", max_length=32)

    class Meta(object):
        verbose_name = u"Голос"
        verbose_name_plural = u"Голоса"
        unique_together = (('photo', 'user_id'), )
