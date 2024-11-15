from django import forms
from django_countries.widgets import CountrySelectWidget
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = {
            'default_phone_number': forms.TextInput(attrs={'autofocus': 'autofocus', 'class': 'form-control'}),
            'default_postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'default_town_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address1': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address2': forms.TextInput(attrs={'class': 'form-control'}),
            'default_county': forms.TextInput(attrs={'class': 'form-control'}),
            'anniversary_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'birthday_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'favorite_flowers': forms.TextInput(attrs={'class': 'form-control'}),
        }