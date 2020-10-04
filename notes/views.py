from datetime import datetime, timezone
from threading import Lock

from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import TemplateView
from notes.models import Note


class NotesView(TemplateView):
    template_name = "notes/notes.html"

    def get_context_data(self, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        context.update(notes=list(Note.objects.all()))
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        if request.POST.get("title", "") != "" and request.POST["text"] != "":
            Note.objects.create(
                title=request.POST["title"],
                text=request.POST["text"],
                date=datetime.now(timezone.utc),
            )
        return HttpResponseRedirect(request.path)
