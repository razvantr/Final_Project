from django.urls import path
from ride import views

urlpatterns = [
    path('create_ride/', views.RideCreateView.as_view(), name='create-ride'),
    path('list_of_rides/', views.RideListView.as_view(), name='list-of-rides'),
    path('delete_ride/<int:pk>/', views.RideDeleteView.as_view(), name='delete-ride'),
    path('search/', views.search, name='search'),
]
