from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from ride.forms import RideForm
from ride.models import Ride


# Create your views here.
class RideCreateView(CreateView):
    template_name = 'ride/create_ride.html'
    model = Ride
    form_class = RideForm
    success_url = reverse_lazy('list-of-rides')

    def form_valid(self, form):
        pass


class RideListView(ListView):
    template_name = 'ride/list_of_rides.html'
    model = Ride
    context_object_name = 'all_rides'


class RideDeleteView(DeleteView):
    template_name = 'ride/delete_ride.html'
    model = Ride
    success_url = reverse_lazy('list-of-rides')


def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        rides = Ride.objects.filter(Q(starting_at__icontains=get_value) | Q(ending_at__icontains=get_value))
    else:
        rides = Ride.objects.all()

    return render(request, 'ride/list_of_rides.html', {'all_rides': rides})
