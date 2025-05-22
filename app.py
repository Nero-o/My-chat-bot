from flask import Flask, request, jsonify
from config import Config
import requests
import json
import os

# não mude o __name__
app = Flask(__name__)

# API Key do Gemini - Carregada de variável de ambiente
# vai manter apenas últimas 10 mensagens 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Dicionário para guardar contexto das conversas
contextos = {}

def extrair_dados_mensagem(data):
    """Extrai informações importantes da mensagem recebida"""
    try:
        entry = data['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']

        if 'messages' in value:
            message = value['messages'][0]
            return {
                'remetente': message['from'],
                'mensagem': message['text']['body'],
                'id_mensagem': message['id'],
                'timestamp': message['timestamp']
            }
        else:
            # Não é mensagem de usuário, pode ser status
            return None
    except (KeyError, IndexError):
        return None

def gerar_resposta_gemini(mensagem, contexto=[]):
    """Gera resposta usando Gemini (Google AI)"""
    if not GEMINI_API_KEY:
        return "❌ API Key do Gemini não configurada!"
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    
    # Prompt sistema personalizado - CUSTOMIZE AQUI
    prompt_sistema = {
        "role": "user", 
        "parts": [{"text": "Você é um assistente virtual brasileiro amigável e prestativo. Responda de forma natural, simpática e útil. Use emojis quando apropriado. Seja sempre educado e mantenha um tom profissional mas descontraído."}]
    }    # você pode modificar pra ficar do seu jeito "parts": [{"text": "Você é um assistente virtual da [SUA EMPRESA]. Responda de forma profissional..."}]
    
    data = {
        "contents": [prompt_sistema] + contexto + [
            {"role": "user", "parts": [{"text": mensagem}]}
        ]
    }
    params = {"key": GEMINI_API_KEY}
    
    try:
        print(f"🧠 Consultando Gemini para: {mensagem}")
        response = requests.post(url, headers=headers, params=params, json=data, timeout=15)
        
        if response.status_code == 200:
            resposta = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            print(f"✅ Resposta do Gemini: {resposta[:100]}...")
            return resposta
        else:
            print(f"❌ Erro na API Gemini: {response.status_code}")
            print(response.text)
            return "Desculpe, estou com dificuldades técnicas no momento. Tente novamente em alguns segundos! 🤖"
    except requests.exceptions.Timeout:
        print("⏰ Timeout na API do Gemini")
        return "Desculpe, demorei muito para responder. Pode repetir a pergunta? ⏱️"
    except Exception as e:
        print(f"❌ Erro completo no Gemini: {e}")
        print(f"❌ Tipo do erro: {type(e)}")
        if hasattr(e, 'response'):
            print(f"❌ Response: {e.response}")
        return "Ops! Algo deu errado aqui. Tente novamente! 😅"

def enviar_mensagem(phone_number, message):
    """Envia mensagem via WhatsApp Business API"""
    headers = {
        'Authorization': f'Bearer {Config.WHATSAPP_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'messaging_product': 'whatsapp',
        'to': phone_number,
        'type': 'text',
        'text': {
            'body': message
        }
    }
    
    try:
        response = requests.post(Config.WHATSAPP_API_URL,
                               headers=headers,
                               json=payload)
        if response.status_code == 200:
            print(f"✅ Mensagem enviada para {phone_number}")
            return True
        else:
            print(f"❌ Erro ao enviar mensagem: {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

@app.route('/')
def home():
    return "WhatsApp Chatbot com Gemini está rodando! 🤖🧠"

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """Verificação do webhook pelo WhatsApp"""
    verify_token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if verify_token == Config.VERIFY_TOKEN:
        return challenge
    else:
        return 'Token inválido', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    """Recebe e processa mensagens do WhatsApp"""
    data = request.get_json()
    print("📨 Dados recebidos:", json.dumps(data, indent=2))

    # Extrair dados da mensagem
    dados_mensagem = extrair_dados_mensagem(data)

    if not dados_mensagem:
        print("⚠️ Evento recebido não é mensagem de usuário (status de entrega). Ignorando.")
        return jsonify({'status': 'ignored'}), 200

    remetente = dados_mensagem['remetente']
    mensagem = dados_mensagem['mensagem']

    print(f"👤 Remetente: {remetente}")
    print(f"💬 Mensagem: {mensagem}")

    # Recuperar contexto da conversa
    contexto = contextos.get(remetente, [])
    
    # Gerar resposta com Gemini
    resposta = gerar_resposta_gemini(mensagem, contexto)

    print(f"🤖 Resposta: {resposta}")

    # Atualizar contexto (manter apenas últimas 10 mensagens)
    contexto.append({"role": "user", "parts": [{"text": mensagem}]})
    contexto.append({"role": "model", "parts": [{"text": resposta}]})
    contextos[remetente] = contexto[-10:]  # Manter apenas últimas 5 trocas

    # Enviar resposta
    enviar_mensagem(remetente, resposta)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    print("🚀 Iniciando WhatsApp Chatbot com Gemini...")
    print("🤖 Chatbot com IA Gemini ativo!")
    print("📱 Aguardando mensagens...")
    app.run(debug=True, host='0.0.0.0', port=5000)