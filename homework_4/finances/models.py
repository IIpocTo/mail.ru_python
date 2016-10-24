from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse


class Charge(models.Model):
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return str(self.date) + " " + str(self.value)

    @staticmethod
    def get_absolute_url():
        return reverse("charges:finances")
