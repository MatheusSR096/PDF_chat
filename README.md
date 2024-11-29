Aqui está um modelo para o seu README, explicando as partes essenciais do código:

---

# **Simple_bot: Converse com seu PDF** 📄

Um chatbot RAG (Retrieval-Augmented Generation) construído com **Streamlit**, **LangChain** e **Hugging Face**, permitindo que os usuários carreguem documentos PDF e façam perguntas com base no conteúdo.

---

## **🚀 Funcionalidades**
- **Carregamento de PDFs:** Os usuários podem carregar arquivos PDF diretamente.
- **Processamento de documentos:** Os PDFs são divididos em chunks para vetorização eficiente.
- **Busca de informações:** Respostas são geradas com base no conteúdo do documento.
- **Interface amigável:** Construída em **Streamlit** com suporte a chat interativo.

---

## **🛠 Tecnologias Utilizadas**
- **Python**
- **Streamlit** para a interface web.
- **LangChain** para RAG e processamento de textos.
- **Hugging Face** para embeddings e geração de respostas.
- **ChromaDB** como banco de vetores.

---

## **📂 Estrutura do Código**

### **1. Classe `RAGChatbot`**
A classe principal do projeto, que gerencia o pipeline completo:
- **`load_document(pdf_file):`**  
  Carrega e processa arquivos PDF usando `PyPDFLoader`.

- **`process_document(documents):`**  
  Divide o texto em chunks e cria embeddings com `HuggingFaceEmbeddings`. Os vetores são armazenados no `ChromaDB`.

- **`create_conversation_chain():`**  
  Cria a cadeia de conversação usando o modelo LLM hospedado na Hugging Face e um prompt personalizado.

- **`chat(question):`**  
  Realiza perguntas ao modelo e retorna respostas baseadas no conteúdo.

---

### **2. `main()`**
O ponto de entrada do aplicativo:
- **Sidebar:** Carregamento de PDFs.
- **Chat interativo:** Entrada do usuário via `st.chat_input` para fazer perguntas.
- **Mensagens:** Exibe mensagens enviadas pelo usuário e respostas do chatbot.

---

### **3. Prompt Customizado**
O prompt usado para guiar as respostas do modelo:
```text
Baseie-se estritamente no contexto fornecido para responder a pergunta.
Se a resposta não estiver no contexto, indique que não possui informações suficientes.

INSTRUÇÕES IMPORTANTES:
- Forneça uma resposta COMPLETA e DETALHADA.
- NÃO INTERROMPA a resposta no meio.
- Se necessário, use parágrafos adicionais para explicar completamente.
- Garanta que a explicação seja clara e abrangente.
```

---

## **⚙️ Como Usar**
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/Simple_bot.git
   cd Simple_bot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com seu token da Hugging Face:
   ```env
   HF_TOKEN=seu_token
   ```

4. Inicie o aplicativo:
   ```bash
   streamlit run app.py
   ```

5. Carregue um PDF e faça perguntas diretamente no chat.

---

## **🔑 Pontos Essenciais do Código**
- **Carregamento seguro de PDFs:** Arquivos são processados usando `tempfile` para evitar problemas de segurança.
- **RAG Pipeline:** Combinação de vetorização (`HuggingFaceEmbeddings` e `ChromaDB`) com modelos LLM para respostas precisas.
- **Interface Streamlit:** Oferece uma experiência fluida e interativa.

---

## **📜 Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para modificar ou expandir este modelo conforme necessário!
### **Desenvolvido por**  
[TheuxSR](https://github.com/TheuxSR) 💻
