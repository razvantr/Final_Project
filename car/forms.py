from django import forms
from django.forms import TextInput, Select
from car.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['plate', 'driver']

        widgets = {
            'plate': TextInput(attrs={'class': 'form-control'}),
            'driver': Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        return cleaned_data


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['plate', 'driver']

        widgets = {
            'plate': TextInput(attrs={'class': 'form-control'}),
            'driver': Select(attrs={'class': 'form-select'})
        }
