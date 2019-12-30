from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView

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


class PackageStatisticView(LoginRequiredMixin, TemplateView):
    template_name = 'post/statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = {
            'Accepted': int(Package.objects.filter(
                status='AC',
                accepted_at__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            ).count()),
            'In transit': int(Package.objects.filter(
                status='TR',
                accepted_at__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            ).count()),
            'Delivered': int(Package.objects.filter(
                status='DV',
                accepted_at__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            ).count()),
            'Rejected': int(Package.objects.filter(
                status='RJ',
                accepted_at__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            ).count())
        }

        plt.bar(d.keys(), d.values())
        plt.xlabel("Status")
        plt.ylabel("Packages")
        plt.savefig("post/static/post/images/statistic.png")

        return context



