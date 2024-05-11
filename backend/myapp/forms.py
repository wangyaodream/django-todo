from django import forms

from .models import InvitationCode


class InvitationCodeForm(forms.Form):
    class Meta:
        model = InvitationCode
        fields = ("code",)