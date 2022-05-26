from django.apps import AppConfig
from django.db.models.signals import post_save



class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'control'

    def ready(self):
        # Conecta implícitamente un controlador de señal decorado con @receiver.
        from . import signals
