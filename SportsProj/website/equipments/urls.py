from django.urls import path
from .views import equipaction
from .views import return_equip

urlpatterns = [
    # URL pattern for the equipment selection page
    path('', equipaction, name='equipments'),
    path('returnequip/',return_equip,name='return_equip')
]
