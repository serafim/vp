# coding=utf-8
from django.views.generic import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = "base.html"


class VideoView(TemplateView):
    template_name = "video.html"

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        context['video_source'] = settings.VIDEO_SOURCE
        return context