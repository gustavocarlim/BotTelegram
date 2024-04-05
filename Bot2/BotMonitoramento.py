from telethon import TelegramClient, sync, events;
from time import sleep;
import requests;
from senhas import api_hash, api_id;

sessao = 'Repassar mensagens'

# def obter_chats():
#     client = TelegramClient(sessao, api_id, api_hash)
#     client.start()
#     dialogs = client.get_dialogs()
#     for dialog in dialogs:
#         print('------------------------')
#         if dialog.id < 0:
#             print(f'Grupo : {dialog.title}')
#             print(f'id : {dialog.id}')
#         else:
#             print(f'Nome: {dialog.title}')
#             print(f'id: {dialog.id}')
#         print('------------------------\n')
        
#     client.disconnect()

# if __name__ == "__main__":
#     obter_chats()

def enviar_mensagem(mensagem):
    bot_token = '5999496290:AAELPcOJt1sW2jdy2SqsKG11NAa2fvDqwsY'
    chat = '-4001998005'
    URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat}&text={mensagem}'
    requests.post(URL)

def enviar_media(chat, event):
    if event.media:
        if event.photo:
            # Se for uma mensagem com uma foto
            event.download_media(file='temp.jpg')
            event.client.send_file(chat, 'temp.jpg', caption=event.text)
        elif event.document:
            # Se for uma mensagem com um documento (pode ser uma imagem)
            event.download_media(file='temp.jpg')
            event.client.send_file(chat, 'temp.jpg', caption=event.text)
        elif event.web_preview:
            # Se for uma mensagem com um link (web preview)
            enviar_mensagem(event.text, chat)

def main():
    print('Monitoramento 2 iniciado')
    client = TelegramClient(sessao, api_id, api_hash)

    @client.on(events.NewMessage(chats=[4046861331]))
    async def handle_new_message(event):
        chat = '-4001998005'  # Chat de destino
        if event.text:
            # Se for uma mensagem de texto
            enviar_mensagem(event.text, chat)
        else:
            # Se for uma mensagem com mídia ou link
            enviar_media(chat, event)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()