from django import forms
from django.forms import TextInput, Select
from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'ride']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'ride': Select(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        return cleaned_data
