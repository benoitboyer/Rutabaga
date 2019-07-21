from django.db import models
from django.conf import settings


class Feed(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    site_url = models.URLField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feeds"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.url
