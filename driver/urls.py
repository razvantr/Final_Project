from django.urls import path
from driver import views

urlpatterns = [
    path('create_driver/', views.DriverCreateView.as_view(), name='create-driver'),
    path('list_of_drivers/', views.DriverListView.as_view(), name='list-of-drivers'),
    path('update_driver/<int:pk>/', views.DriverUpdateView.as_view(), name='update-driver'),
    path('details_driver/<int:pk>/', views.DriverDetailView.as_view(), name='details-driver'),
]
