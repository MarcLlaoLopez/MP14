import telegram
import subprocess
import asyncio

async def main():
    # Reemplaza <TOKEN> con tu token de Telegram
    bot_token = '6145372647:AAEfGTOdaCJReb_n0KjpEko-o5-B-XCTt8M'
    bot = telegram.Bot(token=bot_token)
    
    # Reemplaza <CHAT_ID> con el ID de chat de Telegram al que deseas enviar los resultados
    chat_id = '-4105956972'

    # Solicitar al usuario que escriba el mensaje a enviar
    message_text = input("Escribe el mensaje que deseas enviar al bot de Telegram: ")

    # Envía el mensaje a través de Telegram
    await bot.send_message(chat_id=chat_id, text=message_text)

# Ejecuta la función principal
asyncio.run(main())
