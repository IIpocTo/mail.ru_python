from datetime import date
from decimal import Decimal

from django import forms

from .models import Charge, Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "number"
        ]


class ChargeGoToForm(forms.Form):
    class Meta:
        fields = []


class AccountLookForForm(forms.Form):
    number = forms.CharField(
        max_length=12,
        min_length=12
    )

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        account = Account.objects.filter(number=number)
        if account is not None:
            return cleaned_data
        else:
            self.add_error("number", "There is no such object in database!")
        return cleaned_data


class ChargeForm(forms.ModelForm):


