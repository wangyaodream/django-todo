from django import forms

from .models import CommonUser


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = CommonUser
        fields = ("name", "password")

        widgets = {
            "password": forms.PasswordInput()
        } 


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = CommonUser
        fields = ("name", "email", "password", "remarks")

        widgets = {
            "password": forms.PasswordInput()
        }