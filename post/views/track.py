from django.views.generic import TemplateView
from django.shortcuts import redirect


class TrackView(TemplateView):
    template_name = 'post/track.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        return redirect('track_result', 42)


class TrackResultView(TemplateView):
    template_name = 'post/track_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
