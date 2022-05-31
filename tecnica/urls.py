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
from .entradas_tecnica import DocumentosTecnicaView, NuevoDocumentoTecnicaView, EditarDocumentoTecnicaView, EliminarDocumentoTecnicaView
from .salidas_tecnica import SalidaTecnicaView, NuevoSalidaTecnicaView, EditarSalidaTecnicaView, EliminarSalidaTecnicaView

urlpatterns = [
    path('entradas_tecnica/', DocumentosTecnicaView.as_view(), name="tecnica_entrada"),
    path('crear_tecnica/', NuevoDocumentoTecnicaView.as_view(), name="nuevo_entrada_tecnica"),
    path('editar_tecnica/', EditarDocumentoTecnicaView.as_view(), name="editar_entrada_tecnica"),
    path('eliminar_tecnica/', EliminarDocumentoTecnicaView.as_view(), name="eliminar_entrada_tecnica"),
    path('salidas_tecnica/', SalidaTecnicaView.as_view(), name="tecnica_salida"),
    path('crear_salidas_tecnica/', NuevoSalidaTecnicaView.as_view(), name="nuevo_tecnica_salida"),
    path('editar_salidas_tecnica/', EditarSalidaTecnicaView.as_view(), name="editar_tecnica_salida"),
    path('eliminar_salidas_tecnica/', EliminarSalidaTecnicaView.as_view(), name="eliminar_tecnica_salida"),

]
