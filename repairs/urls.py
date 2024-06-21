from django.urls import path
from .views import vehicle_selection, get_dropdown_data, home

urlpatterns = [
    path('vehicle-selection/', vehicle_selection, name='vehicle_selection'),
    path('get-dropdown-data/', get_dropdown_data, name='get_dropdown_data'),
    path('', home, name='home'),
]
