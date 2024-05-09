from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class ShortUrl(models.Model):
    longUrl = models.URLField(_("Website URL"), max_length=200)
    longUrl = models.URLField(_("Short URL"), max_length=20)
