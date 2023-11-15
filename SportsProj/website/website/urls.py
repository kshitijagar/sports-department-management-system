"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from signup.views import signaction
from login.views import loginaction
from home.views import homeaction
from equipments.views import equipaction
from courts.views import courtaction
from achievements.views import achieveaction
from equipments.views import return_equip
from add_ach.views import addachaction
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction),
    path('login/' ,loginaction),
    path('home/', homeaction),
    path('equipments/', include('equipments.urls')),
    path('courts/',courtaction),
    path('achievement/',achieveaction),
    path('add_achievement/', addachaction)]