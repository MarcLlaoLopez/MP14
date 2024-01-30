#!/usr/bin/env python3
import requests
import telegram

# Definir el token del bot
bot_token = 'TU_TOKEN_AQUÍ' # Reemplaza con tu token
# Inicializar el bot
bot = telegram.Bot(token=bot_token)
# ID de chat de destino (puede ser tu propio chat o un grupo)
chat_id = 'ID_DEL_CHAT_AQUI' # Reemplaza con el ID de chat de destino
# Mensaje que deseas enviar
message = 'Hola, este es un mensaje automático.'
# Envía el mensaje
bot.send_message(chat_id=chat_id, text=message)