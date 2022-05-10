"""scd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from .views import inicio
from .entradas import DocumentosListView, NuevoDocumentoView, EditarDocumento, EliminarDocumento
from .salidas import salidas


urlpatterns = [
    path('', inicio, name="home"),
    path('entradas/', DocumentosListView.as_view(), name="entradas"),
    path('crear_entradas/', NuevoDocumentoView.as_view(), name="crear_entradas"),
    path('editar_entradas/', EditarDocumento.as_view(), name="editar_entradas"),
    path('eliminar_entradas/', EliminarDocumento.as_view(), name="eliminar_entradas"),
    path('salidas/', salidas, name="salidas"),
]
