from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.db.models import CreatedModifiedModel
from .enuns import CarColors, CarModels
from ..person.models import Person


class Car(CreatedModifiedModel, models.Model):
    """
    Car object
    """

    name = models.CharField(verbose_name=_("Name"), max_length=150)
    model = models.CharField(
        verbose_name=_("Model"), max_length=15, choices=CarModels.choices
    )
    color = models.CharField(
        verbose_name=_("Model"), max_length=15, choices=CarColors.choices
    )
    person = models.ForeignKey(
        verbose_name=_("Person"),
        to=Person,
        on_delete=models.PROTECT,
        related_name="cars",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return f"{self.name} ({self.model}/{self.color})"
