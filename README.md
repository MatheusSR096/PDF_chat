# **Simple_bot: Converse com seu PDF 📄**

## **Descrição do Projeto**
O **Simple_bot** é um chatbot interativo que permite conversar com documentos PDF. Baseado em **RAG (Retrieval-Augmented Generation)**, ele utiliza tecnologias avançadas de **Processamento de Linguagem Natural (PLN)** para analisar e responder perguntas com base no conteúdo de PDFs carregados pelo usuário.

Com uma interface construída em **Streamlit**, o Simple_bot é uma ferramenta prática para profissionais, estudantes ou qualquer pessoa que precise extrair informações de documentos de maneira ágil e eficiente.

---

## **Funcionalidades**
- **Carregamento de PDFs**: Faça upload de documentos para análise.
- **Segmentação Inteligente de Texto**: Divide o conteúdo em chunks para vetorização.
- **Busca Vetorial**: Utiliza embeddings para localizar respostas precisas no documento.
- **Respostas Contextuais**: Responde a perguntas baseando-se estritamente no conteúdo carregado.
- **Interface Simples e Intuitiva**: Desenvolvido com Streamlit para fácil interação.

---

## **Tecnologias Utilizadas**
- **Frontend**: [Streamlit](https://streamlit.io/)
- **NLP e Embeddings**: 
  - Modelo de embeddings: `sentence-transformers/all-MiniLM-L6-v2`.
  - Endpoint Hugging Face: `mistralai/Mistral-7B-Instruct-v0.3`.
- **Armazenamento Vetorial**: [ChromaDB](https://www.trychroma.com/).
- **Divisão de Texto**: `RecursiveCharacterTextSplitter` da biblioteca LangChain.
- **Backend**: 
  - [LangChain](https://langchain.com/) para cadeia de processamento.
  - [Hugging Face API](https://huggingface.co/inference-api) para geração de respostas.
- **Gerenciamento de Ambientes**: [Python-dotenv](https://pypi.org/project/python-dotenv/).

---

## **Pré-requisitos**
1. **Python 3.9+**.
2. Conta na [Hugging Face](https://huggingface.co/) para obter o token de API.
3. Dependências instaladas via `requirements.txt` (veja abaixo).

---

## **Instalação**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/simple_bot.git
   cd simple_bot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` e adicione seu token da Hugging Face:
   ```bash
   HF_TOKEN=seu_token_huggingface
   ```

4. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```

---

## **Como Usar**
1. **Carregue seu PDF**: No menu lateral, selecione e faça upload de um arquivo PDF.
2. **Faça Perguntas**: Use o campo de entrada para digitar sua pergunta sobre o conteúdo.
3. **Obtenha Respostas**: O chatbot processará a pergunta e retornará uma resposta clara e detalhada baseada no contexto do PDF.

---

## **Exemplo**
1. **PDF carregado**: "Guia de introdução à Programação".
2. **Pergunta do usuário**: "O que é uma variável em programação?"
3. **Resposta do bot**: 
   > "Uma variável é um espaço na memória do computador usado para armazenar valores que podem ser alterados durante a execução de um programa."

---

## **Contribuições**
Sinta-se à vontade para contribuir com melhorias ou relatórios de bugs. Envie pull requests ou abra issues no repositório!

---

## **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).

---

### **Desenvolvido por**  
[TheuxSR](https://github.com/TheuxSR) 💻
