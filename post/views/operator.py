from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import redirect

from post.models import Package


class OperatorView(LoginRequiredMixin, TemplateView):
    template_name = 'post/operator.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        package = Package.objects.filter(tracking_number=request.POST.get('tracking_number')).first()
        if not package:
            raise Http404

        return redirect('edit_package', package.pk)
