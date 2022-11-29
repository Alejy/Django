"""Proyect1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Proyect1.views import prueba, prueba_two, prueba_three, prueba_four, prueba_five, prueba_six, prueba_seven, prueba_eight, prueba_nine, prueba_ten, plantilla_incrustada, herencias_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba),
    path('prueba_two/', prueba_two),
    path('prueba_three/', prueba_three),
    path('prueba_four/<int:edad>/<int:ano>', prueba_four),
    path('prueba_five/', prueba_five),
    path('prueba_six/', prueba_six),
    path('prueba_seven/', prueba_seven),
    path('prueba_eight/', prueba_eight),
    path('prueba_nine/', prueba_nine),
    path('prueba_ten/', prueba_ten),
    path('plantilla_incrustada/', plantilla_incrustada),
    path('herencias_html/', herencias_html),
]
