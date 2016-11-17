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
	class Meta:
		model = Charge
		fields = ("value", "date")

	def clean(self):
		cleaned_data = super().clean()
		value = cleaned_data.get('value')
		charge_date = cleaned_data.get('date')

		if type(charge_date) != Datetime:
			self.add_error("date", "The date is not correct")
		if value is None or date is None:
			return cleaned_data
		if Decimal.compare(Decimal(0), value) == Decimal('0'):
			self.add_error("value", "Charge can't be a zero value")
		if value < 0 and charge_date > date.today():
			self.add_error("date", "You can't set negative charge on future day")
		return cleaned_data
