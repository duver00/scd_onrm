
from django.db.models.signals import post_save
from django.dispatch import receiver
from control.models import Documento
from django.core.mail import send_mail

def envio_correo(recibe, dirigido):
    last = Documento.objects.all().last()
    titulo = last.titulo
    no_entrada = last.no_entrada_doc
    entidad = last.entidad
    provincia = last.provincia
    organismo = last.organismo
    tdocumento = last.t_documento
    asunto = "Entrada de Nuevo Documento"
    envia = "Sistema de Control Documental <control@onrm.minem.cu>"
    mensaje = f" Aviso de entrada de  un documento para la {dirigido}\n" \
              f"  Número de entrada: {no_entrada}\n" \
              f" Título {titulo}\n" \
              f" Entidad: {entidad}\n" \
              f" Organismo: {organismo}\n" \
              f" Provincia: {provincia}\n" \
              f" Tipo de documento: {tdocumento}\n"
    recpt_list = ['duvergel@onrm.minem.cu']
    send_mail(asunto, mensaje, envia, recibe, fail_silently=False)



@receiver(post_save, sender=Documento)
def notificar_entrada(sender, **kwargs):
    try:
        last_signal = Documento.objects.all().last()
        dirigido_registro = last_signal.dirigido
        dirigido_tecnica = last_signal.dirigido
        if str(dirigido_registro) == 'Dirección de Registro y Control':
            envio_correo(recibe=["Dirección de Registro y Control <duvergel@onrm.minem.cu>"], dirigido=dirigido_registro)
        elif str(dirigido_registro) == 'Dirección Técnica':
            envio_correo(recibe=["Dirección Técnica<duvergel@onrm.minem.cu>"], dirigido=dirigido_tecnica)
    except Exception as e:
        print(e)






