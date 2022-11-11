from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedModifiedModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), editable=False, blank=True, auto_now=True
    )

    class Meta:
        abstract = True
