from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models


class Account(models.Model):
    number = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return str(self.number)

    @staticmethod
    def get_absolute_url():
        return reverse("charges:main")


class Charge(models.Model):
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=datetime.today)
    account = models.ForeignKey(Account)

    def __str__(self):
        return str(self.date) + " " + str(self.value)

    @staticmethod
    def get_absolute_url():
        return reverse("charges:finances")
