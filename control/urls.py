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
from .views import inicio,custom403
from .entradas import DocumentosTemplateView, NuevoDocumentoView, EditarDocumento, EliminarDocumento
from .salidas import DocumentoSalidaTemplateView, NuevoDocumentoSalidaView, EditarDocumentoSalidasView, EliminarDocumentoSalidasView



urlpatterns = [
    path('', inicio, name="home"),
    path('', custom403, name="403"),
    path('entradas/', DocumentosTemplateView.as_view(), name="entradas"),
    path('crear_entradas/', NuevoDocumentoView.as_view(), name="crear_entradas"),
    path('editar_entradas/', EditarDocumento.as_view(), name="editar_entradas"),
    path('eliminar_entradas/', EliminarDocumento.as_view(), name="eliminar_entradas"),
    path('salidas/', DocumentoSalidaTemplateView.as_view(), name="salidas"),
    path('crear_salidas/', NuevoDocumentoSalidaView.as_view(), name="crear_salidas"),
    path('editar_salidas/', EditarDocumentoSalidasView.as_view(), name="editar_salidas"),
    path('eliminar_salidas/', EliminarDocumentoSalidasView.as_view(), name="eliminar_salidas"),
]
