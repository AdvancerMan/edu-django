from . import views
from django.urls import path


urlpatterns = [
    path("", views.NotesView.as_view(), name="notes"),
]
