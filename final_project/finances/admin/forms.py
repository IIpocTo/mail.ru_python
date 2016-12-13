from django import forms
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from ..models import Charge, Account, UserProfile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username", "email", "phone", "address", "first_name", "last_name"]
        widgets = {
            "phone": PhoneNumberPrefixWidget,
            "username": forms.HiddenInput()
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        user = UserProfile.objects.get(username=username)
        phone_number = self.cleaned_data.get('phone')
        user_phone = UserProfile.objects.filter(phone=phone_number)
        print(user_phone.get().id)
        print(user.id)
        if user is not None:
            if len(user_phone) == 0:
                return self.cleaned_data
            else:
                if user_phone.get() == user:
                    return self.cleaned_data
                else:
                    self.add_error("phone", "This phone number is busy!")
        else:
            self.add_error("username", "There is no such object in database!")
        return self.cleaned_data


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username"]

    def clean(self):
        username = self.cleaned_data.get('username')
        user = UserProfile.objects.filter(username=username)
        if user is not None:
            return self.cleaned_data
        else:
            self.add_error("There is no such user!")
