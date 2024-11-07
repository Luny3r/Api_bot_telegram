#importando a biblioteca telebot

import telebot

#criando a variável token e id para adicionar seus valores, respectivamente

token = '7810782597:AAEyoUg-Ou5j2wK_OpGw9wL9g4Mo4u1x3ls'
id = '5362762984'

bot = telebot.TeleBot(token)

print('Digite seu nome:')
nome = input()
print('Digite a sua idade:')
idade = input()
print('Digite o seu CPF:')
n_cpf = input()

def send_telegram_msg(nome, idade, n_cpf):
    msg_final = ('''
        confirmação de cadastro,
        usuário: %s
        nome: %s
        cpf: %s
        Obrigado por criar seu cadastro ^^ !
        '''%(nome, idade, n_cpf))


    sent_msg =  bot.send_message(id, msg_final, parse_mode='Markdown')

send_telegram_msg(nome, idade, n_cpf)