from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """
    Person object
    """

    name = models.CharField(verbose_name=_("Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), editable=False, blank=True, auto_now=True
    )

    @property
    def sale_opportunity(self) -> bool:
        return self.cars.count() < 3

    class Meta:
        ordering = ["name"]
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __str__(self):
        return self.name
