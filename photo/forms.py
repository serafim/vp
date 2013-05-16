# coding=utf-8
from django import forms
from photo.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta(object):
        model = Photo
        fields = ('title', 'author', 'photo', )