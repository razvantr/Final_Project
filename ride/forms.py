from django import forms
from django.forms import Select, DateTimeInput, NumberInput
from ride.models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['starting_at', 'ending_at', 'driver', 'car', 'time', 'price']

        widgets = {
            'starting_at': Select(attrs={'class': 'form-select'}),
            'ending_at': Select(attrs={'class': 'form-select'}),
            'driver': Select(attrs={'class': 'form-select'}),
            'car': Select(attrs={'class': 'form-select'}),
            'time': DateTimeInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        return cleaned_data


class RideUpdateForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['starting_at', 'ending_at', 'driver', 'car', 'time', 'price']

        widgets = {
            'starting_at': Select(attrs={'class': 'form-select'}),
            'ending_at': Select(attrs={'class': 'form-select'}),
            'driver': Select(attrs={'class': 'form-select'}),
            'car': Select(attrs={'class': 'form-select'}),
            'time': DateTimeInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'})
        }
