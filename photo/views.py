# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View, TemplateView
from django.views.generic.edit import CreateView
from photo.forms import PhotoForm
from core.utils import generate_user_id
from photo.models import Photo, Vote


def get_user_id(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = generate_user_id()
    return request.session['user_id']


class UploadView(CreateView):
    form_class = PhotoForm
    template_name = "upload.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_id = get_user_id(self.request)
        instance.save()
        return redirect(reverse('photo', args=[instance.pk]))


class PhotoView(DetailView):
    model = Photo
    template_name = "photo.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        try:
            Vote.objects.get(photo=self.object, user_id=get_user_id(self.request))
            context['vote_available'] = False
        except Vote.DoesNotExist:
            context['vote_available'] = True
        return context


class PhotoListView(ListView):
    model = Photo
    template_name = "list.html"
    context_object_name = "photos"


class VoteView(View):
    def get(self, *args, **kwargs):
        vote = Vote(photo=Photo.objects.get(id=kwargs['pk']), user_id=get_user_id(self.request))
        try:
            vote.save()
        except IntegrityError:
            return HttpResponseForbidden()
        return redirect(reverse('photo', args=[kwargs['pk']]))


class StatsView(TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(user_id=get_user_id(self.request))
        context['user_id'] = get_user_id(self.request)
        return context