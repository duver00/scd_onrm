from django.urls import path
from .views import estadisticas_numeros


urlpatterns = [
path('total/', estadisticas_numeros,name='total_documentos'),
]