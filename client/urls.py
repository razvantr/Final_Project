from django.urls import path

from client import views

urlpatterns = [
    path('create_client/', views.ClientCreateView.as_view(), name='create-client'),
    path('list_of_clients/', views.ClientListView.as_view(), name='list-of-clients'),
    path('delete_client/<int:pk>/', views.ClientDeleteView.as_view(), name='delete-client'),
    path('search/', views.search, name='search'),
]
