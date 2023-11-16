from django.urls import path
from .views import courtaction
from .views import return_court

urlpatterns = [
    # URL pattern for the equipment selection page
    path('', courtaction, name='courts'),
    path('returncourt/',return_court,name='return_court')
]
