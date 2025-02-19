'''
Crie um chatbot com os seguintes recursos:
- O usuario pode solicitar o bot pra ligar ou desligar o ar-condicionado
- O usuario pode informaar uma temperatura desejada para o ar-condicionado
- O usuario pode perguntar a temperatura atual do ar-condicionado
- O usuario pode pedir pra informar a data e hora atual

Utilize as seguintes funções para simular os comandos elétricos do ar-condicionado
'''
import datetime
from groq import Groq
import json 


temp = 20

def ligar_ar_condicionado():
    print('COMANDO PARA LIGAR AR_CONDICIONADO ACIONADOA')

def desligar_ar_condicionado():
    print('COMANDO PARA DESLIGAR AR CONDICIONADO ACIONADO')

def mudar_temperatura_ar_condicionado(temperatura):
    print(f'COMANDO PARA MUDAR A TEMPERATURA DO AR_CONDICIONADO PARA {temperatura} ACIONADO')
    temp = temperatura

def obter_temperatura_ar_condicionado():
    return temp

def obter_data_hora():
    return datetime.datetime.now().strftime('dia %d/%n/%Y hora %H:%M:%S')

prompt_do_usuario = input('O que deseja? ')



client = Groq(api_key='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')

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Isto é um chatbot onde o usuário pode dar comandos ou pedir informações. Você deve analisar a mensagem do usuário para identificar sua intenção e dar um JSON como saída no seguinte formato: {\"intencao\": <numero, \"argumentos\": <array>, \"mensagem\": <texto>}. Cada intenção tem um comando que é executado posteriormente em um programa, e esse comando pode ter argumentos e um retorno. No atributo 'intencao' você deve colocar o número da intenção. No atributo 'argumento' você deve colocar um array contendo os argumentos do comando referente a intenção, ou um array vazio caso não haja argumentos. No atributo 'mensagens' você deve colocar uma mensagem educada de resposta ao usuário.  Em casos em que o usuário pede alguma informação, você deve colocar na mensagem um caractere \"@\" no lugar onde a informação solicitada deve ser inserida. Esta informação solicitada será retornada pelo comando relacionado a intenção do usuário, que será executada posteriormente por um script Python Os números de intenção e seus respectivos comandos são descritos a seguir: \n* Número 1 - intenção de ligar o ar-condicionado. Este comando não requer argumentos e não ter retorno. \n* Número 2 - Intenção de desligar o ar-condicionado. Este comando não requer argumentos e não tem retorno.\n* Número 3- intenção de mudar a temperatura do ar-condicionado. Este comando tem um argumento, que é a temperatura que o usuário quer colocar no ar-condicionado ( numero inteiro), e não tem retorno.\n* Número 4- intenção de saber qual temperatura está configurada no ar-condicionado. Este comando não requer argumentos e retorna a temperatura atual do ar-condicionado, que será inserida posteriormente na mensagem para o usuário no lugar onde você colocar um \"@\".\n* Número 5- Intenção de saber a data ou horo atual. Este comando não requer argumentos e retorna a data e a hora atuais.\nCaso o usuário peça algo que não se enquadre em nenhuma das intenções descrita acima, de um JSON com número 0, array de argumentos vazio e uma mensagem dizendo que a intenção não é suportada"
        },
        {
            'role': 'user',
            'content': prompt_do_usuario
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    response_format={"type": "json_object"},
    stop=None,
)

saida_json = (completion.choices[0].message.content)
saida_dados = json.loads(saida_json)

numero_de_intencao = saida_dados['intencao']
argumentos = saida_dados['argumentos']
mensagem = saida_dados['mensagem']

if numero_de_intencao == 1:
    ligar_ar_condicionado()
    print(mensagem)
elif numero_de_intencao == 2:
    desligar_ar_condicionado()
    print(mensagem)
elif numero_de_intencao == 3:
    t = argumentos[0] # Temperatura
    mudar_temperatura_ar_condicionado(t)
    print(mensagem)
elif numero_de_intencao == 4:
    t = obter_temperatura_ar_condicionado()
    mensagem_processada = mensagem.replace('@', f'{t}°C')
    print(mensagem_processada)
elif numero_de_intencao == 5:
    data_hora = obter_data_hora
    mensagem_processada = mensagem.replace('@', data_hora)
    print(mensagem_processada)
else:
    print(mensagem)