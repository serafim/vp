# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from core.views import VideoView
from photo.views import UploadView, PhotoView, PhotoListView, VoteView, StatsView


admin.autodiscover()
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^video', VideoView.as_view(), name="video"),
    url(r'^upload', UploadView.as_view(), name="upload"),
    url(r'^photo/vote/(?P<pk>\d+)', VoteView.as_view(), name="vote"),
    url(r'^photo/(?P<pk>\d+)', PhotoView.as_view(), name="photo"),
    url(r'^stats', StatsView.as_view(), name="stats"),
    url(r'^', PhotoListView.as_view(), name="index"),
)
