from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from post.models import Package


class NewPackageView(LoginRequiredMixin, CreateView):
    template_name = 'post/package_form.html'
    model = Package
    fields = [
        'sender_name',
        'receiver_name',
        'tracking_number',
        'address_from',
        'address_to',
        'price',
        'value',
        'weight',
    ]
    success_url = '/operator'
    login_url = '/login'

    def get_form(self, **kwargs):
        form = super(NewPackageView, self).get_form()
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        return form


class EditPackageView(LoginRequiredMixin, UpdateView):
    template_name = 'post/package_form.html'
    model = Package
    fields = [
        'sender_name',
        'receiver_name',
        'tracking_number',
        'address_from',
        'address_to',
        'status',
        'price',
        'value',
        'weight',
    ]
    success_url = '/operator'
    login_url = '/login'

    def get_form(self, **kwargs):
        form = super(EditPackageView, self).get_form()
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        return form

    def post(self, request, **kwargs):
        if request.POST['status'] == Package.DELIVERED:
            package = Package.objects.get(pk=kwargs.get('pk'))
            package.delivered_at = datetime.now()
            package.save()

        return super(EditPackageView, self).post(request, **kwargs)
