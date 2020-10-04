from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponseRedirect, \
    HttpResponseBadRequest
from django.contrib.auth import authenticate, login


class UrlView(TemplateView):
    template_name = "main/url_shower.html"

    def get_context_data(self, **kwargs):
        context = super(UrlView, self).get_context_data(**kwargs)
        context.update(url=self.request.get_raw_uri(), title="URLer")
        return context


class RegisterView(TemplateView):
    template_name = "main/register.html"

    def post(self, request: HttpRequest, *args, **kwargs):
        if len(User.objects.filter(username="test")) == 0:
            User.objects.create_user(
                username="test",
                password="123"
            )
        return HttpResponseRedirect(reverse("login"))


class LoginView(TemplateView):
    template_name = "main/login.html"

    def post(self, request: HttpRequest, *args, **kwargs):
        if request.POST["login"] == "" or request.POST["password"] == "":
            return HttpResponseBadRequest()
        user = authenticate(request, username=request.POST["login"],
                            password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("notes"))
        return HttpResponseRedirect("")
