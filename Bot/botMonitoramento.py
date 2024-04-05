from telethon import TelegramClient, sync, events;
from time import sleep;
import requests;
from senhas import api_hash, api_id;

sessao = 'Repassar mensagen'

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
    chat = '-1001999285192'
    URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat}&text={mensagem}'
    requests.post(URL)

def main():
    print('Monitoramento iniciado')
    client = TelegramClient(sessao, api_id, api_hash)

    @client.on(events.NewMessage(chats=[1001572889568]))
    async def handle_new_message(event):
        mensagem = event.raw_text
        enviar_mensagem(mensagem)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()