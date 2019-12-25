from django import http
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import authenticate, logout


class LoginView(TemplateView):
    template_name = 'post/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=login, password=password)

        if user is not None:
            return http.HttpResponseRedirect('/operator')
        else:
            return http.HttpResponseRedirect('/login')


class LogoutView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
