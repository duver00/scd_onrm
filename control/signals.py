from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documento
from django.core.mail import send_mail


def last_documento():
    last = Documento.objects.all().last()
    if last.dirigido == 'Dirección de Registro y Control':
        send_mail('Nueva entrada entrada para la  Dirección de Registro y Control',
                  'Tienes un nuevo documento que se le ha dado entrada',
                  'control@onrm.minem.cu',
                  ['duvergel@onrm.minem.cu'],
                  fail_silently=False,
                  )
    else:
        pass


@receiver(post_save, sender=Documento)
def notificar_entrada(sender, **kwargs):
    return print('sdahjshf sjd')
