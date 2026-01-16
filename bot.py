# Menu de opções do bot
menu = ("Olá! Eu sou um bot da empresa tal. Como posso ajudar você hoje?\n"
        "1. Horário de Atendimento\n"
        "2. Número para Contato\n"
        "3. Localização da Empresa"
        "4. Falar com um atendente")


# Função principal do bot
def responder(texto):
    msg = texto.lower().strip().replace("?", "").replace("!", "")

    if msg in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]:
        return menu

    # Dicionário de comandos
    comandos = {
        "1": "🕒 Atendimento: Seg–Sex, 9h às 18h",
        "2": "📞 Contato: (11) 1234-5678",
        "3": "📍 Rua Exemplo, 123, São Paulo, SP",
        "4": "👨‍💼 Um atendente entrará em contato em breve."
    }
    
    return comandos.get(msg, "Desculpe, não entendi sua mensagem. Por favor, escolha uma das opções do menu.")
