from datetime import timedelta, datetime
from decimal import Decimal

from datetimewidget.widgets import DateTimeWidget
from django.core.validators import RegexValidator
from django.forms import Form, ModelForm, CharField, EmailField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from pytz import UTC

from .models import Charge, Account, UserProfile


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["number"]


class RegisterForm(Form):
    username = CharField(max_length=150, min_length=4, validators=[
        RegexValidator(
            r'^[\w]+$',
            message="Username can contain only letters and digits"
        )
    ])
    password = CharField(max_length=128, min_length=4)
    confirm_password = CharField(max_length=128, min_length=4, label="Confirm Password")
    email = EmailField(max_length=254, label="Email Address")
    phone = PhoneNumberField(max_length=128, widget=PhoneNumberPrefixWidget)
    address = CharField(max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password is None or confirm_password is None:
            return cleaned_data
        if password != confirm_password:
            self.add_error("confirm_password", "Passwords are not the same")
        return cleaned_data


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["last_name", "first_name", "address"]


class LoginForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username", "password"]

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_query = UserProfile.objects.filter(username=username)

        if user_query.count() == 0:
            self.add_error("username", "There is no such user!")
        else:
            user = user_query.get()
            if not user.check_password(password):
                self.add_error("password", "Password is not correct!")

        return self.cleaned_data


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ["value", "transactedAt"]
        date_time_options = {
            'todayBtn': 'true',
            'clearBtn': 'true',
            'todayHighlight': 'true',
            'minuteStep': 1
        }
        widgets = {
            'transactedAt': DateTimeWidget(usel10n=True, bootstrap_version=3, options=date_time_options)
        }

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        charge_date = cleaned_data.get('transactedAt')

        if value is None or charge_date is None:
            return cleaned_data
        if value == Decimal(0):
            self.add_error("value", "Charge can't be a zero value")
        is_future_day = (charge_date > (datetime.now() + timedelta(days=1))
                         .replace(hour=0, minute=0, second=0, tzinfo=UTC))
        if value < 0 and is_future_day:
            self.add_error("transactedAt", "You can't set negative charge on future day")
        return cleaned_data
