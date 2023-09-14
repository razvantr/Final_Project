from django import forms
from django.forms import TextInput, EmailInput, DateInput
from driver.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'email', 'date_hired', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'date_hired': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        get_email = cleaned_data.get('email')

        check_email = Driver.objects.filter(email=get_email)
        if check_email:
            msg = 'Email already in use'
            self._errors['email'] = self.error_class([msg])

        return cleaned_data


class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'email', 'date_hired', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'date_hired': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
