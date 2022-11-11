from django.db import models
from django.utils.translation import gettext_lazy as _


class CarColors(models.TextChoices):
    BLUE = "blue", _("Blue")
    GRAY = "gray", _("Gray")
    YELLOW = "yellow", _("Yellow")


class CarModels(models.TextChoices):
    CONVERTIBLE = "convertible", _("Convertible")
    HATCH = "hatch", _("Hatch")
    SEDAN = "sedan", _("Sedan")
