from django.http import HttpRequest, HttpResponseRedirect, \
    HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from .models import Spider


class SpiderView(TemplateView):
    template_name = 'spider/spider.html'

    def get_context_data(self, **kwargs):
        context = super(SpiderView, self).get_context_data(**kwargs)
        context["friends"] = \
            Spider.objects.filter(is_attacker=False).order_by("-creation_time")
        context["enemies"] = \
            Spider.objects.filter(is_attacker=True).order_by("creation_time")
        return context


def silent_parse(parse, errors):
    def wrapper(x):
        try:
            return parse(x)
        except errors:
            return None

    return wrapper


parse_int = silent_parse(int, (ValueError, TypeError))
parse_float = silent_parse(float, (ValueError, TypeError))


def parse_bool(x):
    if x == "True":
        return True
    elif x == "False":
        return False
    else:
        return None


def parse_spider(request_params):
    params = {}
    for param in ["power", "defense", "health"]:
        params[param] = parse_float(request_params.get(param))
    params["is_attacker"] = parse_bool(request_params.get("is_attacker"))
    params["index"] = parse_int(request_params.get("index"))
    return params


class AddSpiderView(View):
    def parse_params(self, request_params):
        params = parse_spider(request_params)
        del params["index"]
        if None in params.values():
            return None
        return params

    def post(self, request: HttpRequest, **kwargs):
        params = self.parse_params(request.POST)
        if params is None:
            return HttpResponseBadRequest()

        Spider.objects.create(**params)
        return HttpResponseRedirect(reverse("spider-field"))


class RemoveSpiderView(View):
    def parse_params(self, request_params):
        params = parse_spider(request_params)
        if params.get("index") is None:
            return None
        return params

    def post(self, request: HttpRequest, **kwargs):
        params = self.parse_params(request.POST)
        if params is None:
            return HttpResponseBadRequest()

        i = params["index"] - 1
        friends = Spider.objects.filter(is_attacker=False) \
            .order_by(f"-creation_time")
        enemies = Spider.objects.filter(is_attacker=True) \
            .order_by(f"creation_time")
        spiders = [*friends, *enemies]

        if i not in range(len(spiders)):
            return HttpResponseBadRequest()
        spiders[i].delete()
        return HttpResponseRedirect(reverse("spider-field"))


class ChangeSpiderView(View):
    def parse_params(self, request_params):
        params = parse_spider(request_params)
        if None in [params.get("is_attacker"), params.get("index")]:
            return None
        return params

    def post(self, request: HttpRequest, **kwargs):
        params = self.parse_params(request.POST)
        if params is None:
            return HttpResponseBadRequest()

        i = params["index"]
        power = params["power"]
        defense = params["defense"]
        health = params["health"]
        friends = Spider.objects.filter(is_attacker=False) \
            .order_by(f"-creation_time")
        enemies = Spider.objects.filter(is_attacker=True) \
            .order_by(f"creation_time")
        spiders = [*friends, *enemies]

        if i not in range(len(spiders)):
            return HttpResponseBadRequest()
        spider = spiders[i]

        if power is not None:
            spider.power = power
        if defense is not None:
            spider.defense = defense
        if health is not None:
            spider.health = health
        spider.save()
        return HttpResponseRedirect(reverse("spider-field"))
