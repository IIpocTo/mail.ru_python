from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models


class Account(models.Model):
    number = models.CharField(verbose_name="Account number", max_length=12, unique=True, validators=[
        RegexValidator(
            r'^\d+$',
            message="Account number must contains only digits"
        )
    ])
    amount = models.DecimalField(verbose_name="Total account amount", max_digits=16, decimal_places=2)
    owner = models.ForeignKey(User)

    def __str__(self):
        return str(self.number) + " " + str(self.amount) + " " + str(self.owner.username)


class Charge(models.Model):
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=datetime.today)
    account = models.ForeignKey(Account)

    def __str__(self):
        return "( " + str(self.date) + " )" + " " + str(self.value) + " -> " + str(self.account)