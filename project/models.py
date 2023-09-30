from django.db import models

class shortURL(models.Model):
    short_url = models.CharField(max_length=100)
    og_url = models.URLField(max_length=700)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_url