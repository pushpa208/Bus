# from django.urls import path
# from .views import BusListView, AddBusView

# urlpatterns = [
#     path('buses/', BusListView.as_view(), name='bus-list'),
#     path('add-bus/', AddBusView.as_view(), name='add-bus'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('buses/', views.bus_list, name='bus-list'),# Bus list
    path('add-bus/', views.add_bus, name='add-bus'),# Add bus
    path('edit-bus/<int:pk>/', views.edit_bus, name='edit-bus'),  # Edit bus
    path('delete-bus/<int:pk>/', views.delete_bus, name='delete-bus'),  # Delete bus
]
