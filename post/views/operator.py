from django.views.generic import TemplateView


class OperatorView(TemplateView):
    template_name = 'post/operator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def post(self, request, *args, **kwargs):
    #     package = Package.objects.filter(tracking_number=request.POST.get('tracking_number')).first()
    #     if not package:
    #         raise Http404
    #     return redirect('track_result', package.pk)
