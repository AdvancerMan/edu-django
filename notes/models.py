from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"[{self.date}] {self.title}: {self.text}"
