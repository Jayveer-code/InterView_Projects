from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    summary = models.TextField(blank=True)
    source = models.CharField(max_length=100)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
