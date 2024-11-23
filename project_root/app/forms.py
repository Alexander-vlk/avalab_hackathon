from django import forms

from app.models import UserData


FIELD_STYLE_CLASS = "w-full px-5 py-1 text-gray-700 bg-gray-200 rounded my-3" 


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
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Название бизнеса',
                    }
                ),
            'business_type': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Тип бизнеса',
                    }
                ),
            'region': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Регион',
                    }   
                ),
            'industry': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Отрасль',
                    }
                ),
        }
        