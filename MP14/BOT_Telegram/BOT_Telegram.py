#!/usr/bin/env python3
import requests

idBot = '586663935'
idGrupo = '-4109128386'

def enviarMensaje(mensaje):
    requests.post('6145372647:AAFnUWYbcJ1LW9Qv6f9gAuQ98Ez5c5q1HAI' + idBot + '/sendMessage',
              data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})

def enviarDocumento(ruta):
    requests.post('6145372647:AAFnUWYbcJ1LW9Qv6f9gAuQ98Ez5c5q1HAI' + idBot + '/sendDocument',
              files={'document': (ruta, open(ruta, 'rb'))},
              data={'chat_id': idGrupo, 'caption': 'imagen caption'})
    
enviarMensaje("Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python")
enviarDocumento("esta/es/la/ruta/completa/del/documento.jpg")