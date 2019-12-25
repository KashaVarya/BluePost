from django import http
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout


class LoginView(TemplateView):
    template_name = 'post/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            return http.HttpResponseRedirect('/operator')
        else:
            return http.HttpResponseRedirect('/login')


class LogoutView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
