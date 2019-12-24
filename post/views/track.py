from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.http import Http404

from post.models import Package


class TrackView(TemplateView):
    template_name = 'post/track.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        package = Package.objects.filter(tracking_number=request.POST.get('tracking_number')).first()
        if not package:
            raise Http404
        return redirect('track_result', package.pk)


class TrackResultView(DetailView):
    template_name = 'post/track_result.html'
    model = Package

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
