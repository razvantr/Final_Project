from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from driver.forms import DriverForm, DriverUpdateForm
from driver.models import Driver


# Create your views here.
class DriverCreateView(CreateView):
    template_name = 'driver/create_driver.html'
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy('list_of_drivers')

    def form_valid(self, form):
        pass


class DriverListView(ListView):
    template_name = 'driver/list_of_drivers.html'
    model = Driver
    context_object_name = 'all_drivers'


class DriverUpdateView(UpdateView):
    template_name = 'driver/update_driver.html'
    model = Driver
    form_class = DriverUpdateForm
    success_url = reverse_lazy('list-of-drivers')


class DriverDetailView(DetailView):
    template_name = 'driver/details_driver.html'
    model = Driver
