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
from .views import NomencladoresView, NuevoNomencladorView, EditarNomencladorView, EliminarNomencladorView


urlpatterns = [
    path('nomencladores/', NomencladoresView.as_view(), name="nomencladores"),
    path('agregar_nomencladores/', NuevoNomencladorView.as_view(), name="agregar_nomenclador"),
    path('editar_nomencladores/', EditarNomencladorView.as_view(), name="editar_nomenclador"),
    path('eliminar_nomencladores/', EliminarNomencladorView.as_view(), name="eliminar_nomenclador"),
]
