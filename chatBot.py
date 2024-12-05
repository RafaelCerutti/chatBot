import telebot

api_token = "7845492432:AAHqujBawM7fMzn4scAQg5QYo0JbkCQoMOE"

bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['dinheiro'])
def pagamento_dinheiro(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido realizado com sucesso!')

@bot.message_handler(commands=['cartao'])
def pagamento_cartao(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido realizado com sucesso!')

@bot.message_handler(commands=['vr'])
def pagamento_vr(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido realizado com sucesso!')


@bot.message_handler(commands=['combo1'])
def combo1(mensagem):    
    texto =  """
    Seu pedido ficou R$69,90
Qual será a forma de pagamento?
/dinheiro Dinheiro
/cartao Cartão
/vr Vale Refeição
    """
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=['combo2'])
def combo2(mensagem):    
    texto =  """
    Seu pedido ficou R$89,90
Qual será a forma de pagamento?
/dinheiro Dinheiro
/cartao Cartão
/vr Vale Refeição
    """
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=['combo3'])
def combo3(mensagem):  
    texto =  """
    Seu pedido ficou R$119,90
Qual será a forma de pagamento?
/dinheiro Dinheiro
/cartao Cartão
/vr Vale Refeição
    """  
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=['opcao1'])
def fazer_pedido(mensagem):
    texto = """
Combos:    
/combo1 Combo 1 R$69,90 (Dois hamburguers, batata frita, aneis de cebola)
/combo2 Combo 2 R$89,90 (Três hamburguers, batata frita, aneis de cebola)
/combo3 Combo 3 R$119,90 (Quatro hamburgurs, batata frita, aneis de cebola)
"""   
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=['opcao2'])
def acompanhar_pedido(mensagem):
    bot.send_message(mensagem.chat.id,'Seu pedido está em caminho para entrega!')


def verificar(mensagem):
    return True

@bot.message_handler(func= verificar)
def resposta(mensagem):
    texto = """Bem vindo ao X Burguer: 
    /opcao1 Fazer um pedido
    /opcao2 Acompanhar pedido   
"""
    bot.send_message(mensagem.chat.id,texto)

bot.polling()
