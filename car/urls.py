from django.urls import path
from car import views

urlpatterns = [
    path('create_car/', views.CarCreateView.as_view(), name='create-car'),
    path('list_of_cars/', views.CarListView.as_view(), name='list-of-cars'),
    path('update_car/<int:pk>/', views.CarUpdateView.as_view(), name='update-car'),
    path('delete_car/<int:pk>/', views.CarDeleteView.as_view(), name='delete-car'),
    path('details_car/<int:pk>', views.CarDetailView.as_view(), name='details-car'),
]
