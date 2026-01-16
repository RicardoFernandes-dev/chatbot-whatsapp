from flask import Flask, request
from bot import responder
import requests

token = ""
phone_number_id = ""
# Inicializar o aplicativo Flask
app = Flask(__name__)

# Rota para receber mensagens do webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.json

    try:
        mensagem = dados["entry"][0]["changes"][0]["value"]["messages"][0]
        msg = mensagem["text"]["body"]
        numero = mensagem["from"]
    except (KeyError, IndexError):
        return "OK", 200
    
    resposta = responder(msg)
    enviar_mensagem(numero, resposta)
    return "OK", 200

def enviar_mensagem(numero, texto):
    url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "text": { "body": texto }
    }

    response = requests.post(url, headers=headers, json=payload)

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if token == 'seu_token_de_verificacao':
        return challenge
    return "Erro", 403

# Iniciar o servidor Flask   
if __name__ == '__main__':
    app.run(debug=True,port=5000)