from django.urls import path
from . import views


urlpatterns = [
    path("", views.SpiderView.as_view(), name="spider-field"),
    path("add", views.AddSpiderView.as_view(), name="spider-add"),
    path("change", views.ChangeSpiderView.as_view(), name="spider-change"),
    path("remove", views.RemoveSpiderView.as_view(), name="spider-remove"),
]
