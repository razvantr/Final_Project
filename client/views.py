from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from client.forms import ClientForm
from client.models import Client


# Create your views here.
class ClientCreateView(CreateView):
    template_name = 'client/create_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        pass


class ClientListView(ListView):
    template_name = 'client/list_of_clients.html'
    model = Client
    context_object_name = 'all_clients'


class ClientDeleteView(DeleteView):
    template_name = 'client/delete_client.html'
    model = Client
    success_url = 'list-of-clients'
