from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from driver.models import Driver


# Create your views here.
class DriverCreateView(CreateView):
    template_name = 'driver/create_driver.html'
    model = Driver
    form_class = ''
    success_url = reverse_lazy('')

    def form_valid(self, form):
        pass
