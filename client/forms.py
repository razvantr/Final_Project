from django import forms
from django.forms import TextInput, Select
from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'ride']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'ride': Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        return cleaned_data
