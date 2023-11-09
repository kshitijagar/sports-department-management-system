from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the equipment selection page
    path('', views.equipaction, name='equipments'),
]
