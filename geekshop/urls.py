"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main),
    path('catalog/', mainapp.catalog),
    path('catalog/lot_1/', mainapp.lot_1),
    path('catalog/lot_2/', mainapp.lot_2),
    path('catalog/lot_3/', mainapp.lot_3),
    path('contacts/', mainapp.contacts),
    path('admin/', admin.site.urls),
]
