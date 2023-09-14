from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from driver.forms import DriverForm, DriverUpdateForm
from driver.models import Driver, HistoryDriver


# Create your views here.
class DriverCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'driver/create_driver.html'
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy('list_of_drivers')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' was successfully added'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_driver = form.save(commit=False)
            new_driver.first_name = new_driver.first_name.title()
            new_driver.last_name = new_driver.last_name.title()
            new_driver.save()
            get_message = (f'Driver was successfully added. '
                           f'first_name: {new_driver.first_name}, last_name: {new_driver.last_name}, '
                           f'email: {new_driver.email}, user: {self.request.user.id}')
            HistoryDriver.objects.create(message=get_message, created_at=datetime.now(), active=True,
                                         user_id=self.request.user.id)
        return redirect('list-of-drivers')


class DriverListView(LoginRequiredMixin, ListView):
    template_name = 'driver/list_of_drivers.html'
    model = Driver
    context_object_name = 'all_drivers'


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'driver/update_driver.html'
    model = Driver
    form_class = DriverUpdateForm
    success_url = reverse_lazy('list-of-drivers')


class DriverDetailView(LoginRequiredMixin, DetailView):
    template_name = 'driver/details_driver.html'
    model = Driver
