from django.urls import path
from .views import *

app_name = 'insuarance'

urlpatterns = [
    path('add_customer/', add_customer, name='add_customer'),
    path('view_customers/', view_customers, name='view_customers'),
    path('view_customer/<int:customer_id>/', view_customer, name='view_customer'),
    path('add_policy/', add_policy, name='add_policy'),
    path('view_policy/', view_policy, name='view_policy'),
    path('update_policy/', update_policy, name='update_policy'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    path('view_vehicles/', view_vehicles, name='view_vehicles'),
    path('view_vehicle/<str:number_plate>/', view_vehicle, name='view_vehicle'),
    path('dashboard/', dashboard, name='dashboard'),


]
