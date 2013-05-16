# coding=utf-8
from django.contrib import admin
from photo.models import Photo, Vote


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'user_id', )
    list_display_links = ('title', )

admin.site.register(Photo, PhotoAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'user_id', )
    list_display_links = ('id', )

admin.site.register(Vote, VoteAdmin)