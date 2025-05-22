# 🤖 WhatsApp Chatbot com Google Gemini
**Feito por Omar Mahmoud e Thiago Silva**

Chatbot inteligente para WhatsApp Business que utiliza a IA do Google Gemini para conversas naturais e contextualizadas.

## ✨ Funcionalidades

- 💬 **Conversas naturais** com IA Google Gemini
- 🧠 **Contexto mantido** durante a conversa
- 📱 **Integração completa** com WhatsApp Business API
- ⚡ **Respostas automáticas** 24/7
- 🔄 **Deploy fácil** no Railway
- 🌐 **Webhook** para recebimento de mensagens
- 📊 **Logs detalhados** para monitoramento

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** - Framework web
- **Google Gemini API** - Inteligência Artificial
- **WhatsApp Business API** - Integração com WhatsApp
- **Railway** - Deploy e hospedagem

## 🚀 Deploy Rápido no Railway

### 1. Fork este repositório
Clique em "Fork" no GitHub para criar sua cópia.

### 2. Deploy no Railway
1. Acesse [railway.app](https://railway.app/)
2. Faça login com GitHub
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha seu fork do projeto
6. Railway fará o deploy automaticamente!

### 3. Configurar Variáveis de Ambiente
No Railway, vá em **Variables** e adicione:

```env
WHATSAPP_TOKEN=seu_token_do_whatsapp_business
VERIFY_TOKEN=seu_token_de_verificacao_personalizado
PHONE_NUMBER_ID=seu_phone_number_id
GEMINI_API_KEY=sua_chave_da_api_gemini
```

## 🔧 Configuração Detalhada

### 📋 Pré-requisitos

1. **Conta Meta for Developers** - [developers.facebook.com](https://developers.facebook.com/)
2. **Conta Google AI Studio** - [aistudio.google.com](https://aistudio.google.com/)
3. **Conta Railway** - [railway.app](https://railway.app/)

### 🔑 1. Configurar WhatsApp Business API

#### 1.1. Criar App no Meta for Developers

1. Acesse [developers.facebook.com](https://developers.facebook.com/)
2. Clique em "Meus Apps" → "Criar App"
3. Selecione **"Empresa"** como tipo
4. Preencha os dados do app

#### 1.2. Adicionar WhatsApp Business

1. Na dashboard do app, procure **"WhatsApp"**
2. Clique em **"Configurar"**
3. Siga o assistente de configuração

#### 1.3. Obter Tokens

Após configurar, você terá acesso a:

**`WHATSAPP_TOKEN`**: Token de acesso permanente
- 📍 Localização: WhatsApp → Configuration → Access Token
- 🔄 Gere um token permanente (não temporário)

**`PHONE_NUMBER_ID`**: ID do número de telefone
- 📍 Localização: WhatsApp → Configuration → Phone Number ID
- 📝 Exemplo: `710939005425103`

**`VERIFY_TOKEN`**: Token criado por você
- 🔐 Crie uma senha personalizada (ex: `meubot123senha`)
- 📝 Use apenas letras, números e underscore

### 🧠 2. Configurar Google Gemini API

#### 2.1. Obter API Key

1. Acesse [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave gerada

**`GEMINI_API_KEY`**: Sua chave da API Gemini
- 📝 Exemplo: `AIzaSyAbc123def456ghi789...`

### 🌐 3. Configurar Webhook

#### 3.1. Após Deploy no Railway

1. Copie a URL do seu app no Railway
   - 📝 Exemplo: `https://seu-app.up.railway.app`

#### 3.2. Configurar no Meta for Developers

1. Vá em **WhatsApp → Configuration → Webhooks**
2. Configure:
   - **Callback URL**: `https://seu-app.up.railway.app/webhook`
   - **Verify Token**: O mesmo que você colocou em `VERIFY_TOKEN`
3. Selecione os eventos:
   - ✅ **messages**
   - ✅ **message_deliveries**
4. Clique em **"Verify and Save"**

#### 3.3. Adicionar Número de Teste

1. Em **WhatsApp → Configuration**
2. Procure **"Phone numbers for testing"**
3. Adicione seu número no formato: `5571999999999`
4. Confirme por SMS se solicitado

## 📁 Estrutura do Projeto

```
whatsapp-chatbot/
├── app.py              # Aplicação principal Flask
├── config.py           # Configurações e variáveis de ambiente
├── requirements.txt    # Dependências Python
├── .env.example        # Exemplo de configuração
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Esta documentação
```

## 🧪 Testando o Chatbot

### 1. Verificar Deploy

Acesse: `https://seu-app.up.railway.app`
Deve aparecer: "WhatsApp Chatbot com Gemini está rodando! 🤖🧠"

### 2. Enviar Mensagem de Teste

1. Abra o WhatsApp no seu celular
2. Adicione o número de teste (ex: `+1 555 651 0033`)
3. Envie: "Oi, chatbot!"
4. O bot deve responder automaticamente

### 3. Comandos de Exemplo

- `Oi` → Saudação do chatbot
- `Como você funciona?` → Explicação sobre IA
- `Qual é a capital do Brasil?` → Pergunta de conhecimento
- `Me conte uma piada` → Solicitação criativa

## 🔄 Atualização e Manutenção

### Atualizar o Código

1. Faça suas modificações no código
2. Commit e push para o GitHub:
   ```bash
   git add .
   git commit -m "🚀 Atualização do chatbot"
   git push
   ```
3. Railway fará redeploy automaticamente

### Monitorar Logs

No Railway: **Deployments → View Logs**
Monitore mensagens recebidas e erros

### Limites e Custos

- **Railway**: $5/mês (Hobby Plan) para uptime ilimitado
- **Google Gemini**: Gratuito até 15 req/min
- **WhatsApp Business**: Gratuito até 1.000 mensagens/mês

## 🐛 Resolução de Problemas

### Webhook não funciona

1. ✅ Verifique se a URL está correta
2. ✅ Confirme que `VERIFY_TOKEN` é igual nos dois lugares
3. ✅ Teste a URL: `https://seu-app.up.railway.app/webhook`

### Bot não responde

1. ✅ Verifique logs no Railway
2. ✅ Confirme `GEMINI_API_KEY` válida
3. ✅ Seu número está na lista de teste?

### Erro 404 na API Gemini

1. ✅ Verifique se a API Key está correta
2. ✅ Confirme se o modelo `gemini-1.5-flash` está disponível

### Token inválido WhatsApp

1. ✅ Gere novo token permanente
2. ✅ Atualize `WHATSAPP_TOKEN` no Railway
3. ✅ Confirme `PHONE_NUMBER_ID` correto

## 📋 Exemplo de .env

Crie um arquivo `.env` localmente para desenvolvimento:

```env
# WhatsApp Business API
WHATSAPP_TOKEN=EAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
VERIFY_TOKEN=meubot123senha
PHONE_NUMBER_ID=710939005425103

# Google Gemini API  
GEMINI_API_KEY=AIzaSyAxxxxxxxxxxxxxxxxxxxxx
```

⚠️ **IMPORTANTE**: Nunca commite o arquivo `.env` no Git!

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte


- 💬 **Issues**: Use as Issues do GitHub para reportar bugs
- 📚 **Documentação**: [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)

---

> 🚀 **Pronto para começar?** Faça o fork e deploy agora mesmo!
