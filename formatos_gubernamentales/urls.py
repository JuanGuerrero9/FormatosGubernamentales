"""formatos_roxana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.usuario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entidades/', include(('apps.entidades.urls', 'entidades'))),
    path('usuario/', include(('apps.usuario.urls', 'usuario'))),
    path('', PlantillaPrincipal.as_view(), name='plantilla_principal'),
    path('plantilla_inicio', login_required(PlantillaInicio.as_view()), name='plantilla_inicio'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('accounts/login/', Login.as_view(), name='login'),
]
