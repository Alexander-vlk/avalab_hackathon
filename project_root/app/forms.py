from django import forms

from app.models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'name',
            'business_type',
            'region',
            'industry',
            'is_innovative',
        ]
        