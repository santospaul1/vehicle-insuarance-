from django.contrib import admin
from django.urls import path, include  # Import the include function

from insuarance.views import add_customer, view_customers

urlpatterns = [
    path('', view_customers, name='view_customers'),
    path('admin/', admin.site.urls),
    path('', include('insuarance.urls')),  # Include insuarance URLs for the root path
]
