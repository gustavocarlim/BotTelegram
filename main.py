# from typing import FINAL
# from telegram import UPDATE
# from telegram.ext import Application, CommandHandler, MenssageHandler, filters, ContextTypes

# TOKEN: FINAL = '5999496290:AAELPcOJt1sW2jdy2SqsKG11NAa2fvDqwsY'
# BOT_USERNAME: FINAL = '@komodo_repasse_bot'

# async def start_command (update: UPDATE, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Olá! Obrigado por falar comigo...')

# async def help_command (update: UPDATE, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Sou um komodo, escreva para que eu possa te responder!')

# async def custom_command (update: UPDATE, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Isso é um comando customizado')

# def handle_response(text: str) -> str:
#     processed: str = text.lower()

#     if 'oi' in processed:
#         return 'OI AMIGO'

#         if 'como você tá' in processed:
#             return 'TO FELIZZZ'

#     return 'Não entendi o que vc escreveu, sou burro :('

#     async def handle_message(update: UPDATE, context: ContextTypes.DEFAULT_TYPE):
#         message.type: str = update.message.chat.type
#         text: str = update.message.text

#         print (f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#         if message_type = 'group':
#             if BOT_USERNAME in text:
#                 new_text: str = text.replace(BOT_USERNAME, '').strip()
#                 response: str = handle_response(new_text)

#                 else: 
#                     return
#             else:
#                 response: str = handle_response(text)

#                 print ('BOT', response)
#                 await update.message.reply_text(response)

# async def error (update: UPDATE, context:ContextTypes.DEFAULT_TYPE):
#     print (f'UPDATE {update} caused error {context.error}')

#     if __name___== '__main__':
#         app = Application.builder().token(TOKEN).build()

#         app.add_handler(CommandHandler('start', start_command))
#         app.add_handler(CommandHandler('help', help_command))
#         app.add_handler(CommandHandler('custom', custom_command))

#         app.add_handler(MenssageHandler(filters.TEXT, handle_message))

#         app.add_error_handler(error)

#         print ('Polling...')
#         app.run_polling(poll_interval = 3)