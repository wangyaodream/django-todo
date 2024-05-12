from django import forms

from .models import CommonUser


class CommonUserForm(forms.ModelForm):
    class Meta:
        model = CommonUser
        fields = "__all__"