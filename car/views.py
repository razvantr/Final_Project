from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from car.forms import CarForm, CarUpdateForm
from car.models import Car, HistoryCar


# Create your views here.
class CarCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'car/create_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-of-cars')
    success_message = '{plate}'

    def get_success_message(self, cleaned_data):
        message = 'The car with ' + self.success_message + ' was added successfully'
        return message.format(plate=self.object.plate)

    def form_valid(self, form):
        if form.is_valid():
            new_car = form.save(commit=False)
            new_car.plate = new_car.plate
            new_car.save()
            get_message = f'The car was added with success. plate: {new_car.plate}, driver: {new_car.driver}'
            HistoryCar.objects.create(message=get_message, created_at=datetime.now(), user_id=self.request.user.id)
        return redirect('list-of-cars')


class CarListView(LoginRequiredMixin, ListView):
    template_name = 'car/list_of_cars.html'
    model = Car
    context_object_name = 'all_cars'


class CarUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'car/update_car.html'
    model = Car
    form_class = CarUpdateForm
    success_url = reverse_lazy('list-of-cars')


class CarDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'car/delete_car.html'
    model = Car
    success_url = reverse_lazy('list-of-cars')


class CarDetailView(LoginRequiredMixin, DetailView):
    template_name = 'car/details_car.html'
    model = Car
