'''
Crie um chatbot inteligente com Telegram e Groq que tenha os seguintes recursos.

- Ao mandar o comando \start ou \help, o usuario recebe uma mensagem explicando tudo que o chatbot é capaz de falar.

-Ao mandar uma mensagem simples, sem nenhum comando, o Groq deve ser utilizado para fazer a análise de intenção do usuario, exercutar a ação solicitada e dar uma mensagem de resposta.

As operações que o chatbot pode realizar são: 
- Ligar a luz
- Desligar a luz

utilizar as seguintes funções para simular os comandos eletricos de ligar e desligar a luz:
'''

import telebot

API_TOKEN = "7660774456:AAE8OzzO0YFU3EmoQb6oRVdLAkhonXxcBZo"

bot = telebot.TeleBot(API_TOKEN)

def ligar_luz():
    print('COMANDO DE LIGAR LUZ ACIONADO')

def desligar_luz():
    print('COMANDO DE DESLIGAR LUZ ACIONADO')

def analisar_intencao(mensagem):
    if 'ligar luz' in mensagem.lower(): 
        return 'ligar_luz'
    elif 'desliga' in mensagem.lower():
        return 'desligar_luz'
    else:
        return 'comando_desconhecido'
    
@bot.message_handler(commands=['start', 'help'])
def enviar_ajuda(msg):
    resposta = (
        "Olá, eu sou um chatbot inteligente que pode te ajudar a controlar a luz da sua casa.\n"
        "Eu entendo os seguintes comandos:\n"
        "Ligar a luz:\n"
        "Desligar\n"
        "Envie uma mensagem com o comando desejado."
    )
    bot.reply_to(msg, resposta)

@bot.message_handler(func=lambda msg: True)
def responder_mensagem(msg):
    intencao = analisar_intencao(msg.text)
    if intencao == 'ligar_luz':
        ligar_luz()
        bot.reply_to(msg, "A luz foi ligada.")
    elif intencao == 'desligar_luz':
        desligar_luz()
        bot.reply_to(msg, "A luz foi desligada.")
    else:
        bot.reply_to(msg, "Desculpe, não entendi o que você quer.")

bot.infinity_polling()
