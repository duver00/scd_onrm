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
from .entradas_registro import DocumentoRegistroView, NuevoDocumentoRegistroView,EditarDocumentoRegistroView, EliminarDocumentoRegistroView
from .salidas_registro import SalidaRegistroView, NuevaSalidaRegistroView, EditarSalidaRegistroView, EliminarSalidaRegistroView


urlpatterns = [
    path('entradas_registro/', DocumentoRegistroView.as_view(), name="registro_entrada"),
    path('crear_registro/', NuevoDocumentoRegistroView.as_view(), name="nuevo_entrada_registro"),
    path('editar_registro/', EditarDocumentoRegistroView.as_view(), name="editar_entradas_registro"),
    path('eliminar_registro/', EliminarDocumentoRegistroView.as_view(), name="eliminar_entradas_registro"),
    path('salidas_registro/', SalidaRegistroView.as_view(), name="registro_salidas"),
    path('nueva_salida_registro/', NuevaSalidaRegistroView.as_view(), name="nuevo_registro_salidas"),
    path('editar_salida_registro/',EditarSalidaRegistroView.as_view(), name="editar_registro_salidas"),
    path('eliminar_salida_registro/', EliminarSalidaRegistroView.as_view(), name="eliminar_registro_salidas"),



]
