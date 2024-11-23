from django import forms

from app.models import UserData


FIELD_STYLE_CLASS = "w-full px-5 py-3 text-white bg-blue-900 bg-opacity-50 rounded-md my-3" 
 

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
                    'name': 'name',
                    }
                ),
            'business_type': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'name': 'business_type',
                    }
                ),
            'region': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'name': 'region',
                    }   
                ),
            'industry': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'name': 'industry',
                    }
                ),
            'is_innovative': forms.CheckboxInput(
                attrs={
                    'id': 'is_innovative',
                    'name': 'checkbox',
                    }
                ),
        }
        