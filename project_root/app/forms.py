from django import forms

from app.models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        