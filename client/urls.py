from django.urls import path

from client import views

urlpatterns = [
    path('create_client/', views.ClientCreateView(), name='create-client'),
    path('list_of_clients/', views.ClientListView(), name='list-of-clients'),
    path('delete_client/<int:pk>/', views.ClientDeleteView(), name='delete-client'),
]
