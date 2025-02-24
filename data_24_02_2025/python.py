'''
Usando o chatbot do Telegram.
https://pytba.readthedocs.io/en/latest/quick_start.html
Não esquece de importar.
Baixar o telegram tambem e utilizar: BotFather
Retirar o vc sabe oq API

'''
import telebot  

API_TOKEN = "76601998981998774456:AAE8OzzO0YFU3EmoQb6oRVdLAkhonXxcBZo"

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def comando_star(msg):
    print('Mensagem:', msg.text)
    bot.reply_to(msg, "Olá Mundo!")

@bot.message_handler(commands=['teste'])
def comando_teste(msg):
    print('Remetente', msg.from_user.first_name, msg.from_user.last_name)
    print('ID Remetente', msg.from_user.id)
    nome = msg.text.replace('/teste ', '')
    bot.reply_to(msg, f"Olá {nome}!")

@bot.message_handler(func=lambda m: True)
def responder_mensagem(msg):
    bot.reply_to(msg, f"A mensagem recebida foi: {msg.text}")

bot.infinity_polling()
