from flask import Flask, request
# import requests
# import os

app = Flask(__name__)

menu = ("Olá! Eu sou um bot da empresa tal. Como posso ajudar você hoje?\n"
        "1. Horário de Atendimento\n"
        "2. Número para Contato\n"
        "3. Localização da Empresa")

def bot(texto):
    msg = texto.lower().strip().replace("?", "").replace("!", "")

    if msg in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]:
        return menu
    elif msg == "1":
        return "🕒 Atendimento: Segunda à Sexta, das 9h às 18h."
    elif msg == "2":
        return "📞 Contato é (11) 1234-5678."
    elif msg == "3":
        return "📍 Rua Exemplo, 123, São Paulo, SP."
    else:
        return "❌ Desculpe, não entendi sua solicitação. Por favor, escolha uma das opções do menu."
    

@app.route('/webhook', methods=['POST'])
def bot_route():
    dados = request.json
    msg = dados.get["mensagem", ""]
    resposta = bot(msg)
    return {"resposta": resposta}
    

app.run(port=5000)