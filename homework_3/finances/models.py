from django.db import models


class Charge(models.Model):
    currency = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.currency
