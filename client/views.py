from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from client.forms import ClientForm
from client.models import Client, HistoryClient


# Create your views here.
class ClientCreateView(SuccessMessageMixin, CreateView):
    template_name = 'client/create_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home-page')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        message = self.success_message + ' successfully reserved a seat'
        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.first_name = new_client.first_name.title()
            new_client.last_name = new_client.last_name.title()
            new_client.save()
            get_message = (f'Seat successfully reserved. '
                           f'name: {new_client.first_name} {new_client.last_name}, '
                           f' ride: {new_client.ride}')
            HistoryClient.objects.create(message=get_message, created_at=datetime.now(), user_id=self.request.user.id)
        return redirect('home-page')


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'client/list_of_clients.html'
    model = Client
    context_object_name = 'all_clients'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'client/delete_client.html'
    model = Client
    success_url = 'list-of-clients'


@login_required()
def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        clients = Client.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
    else:
        clients = Client.objects.all()

    return render(request, 'client/list_of_clients.html', {'all_clients': clients})
