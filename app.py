import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

class RAGChatbot:
    def __init__(self):
        self.conversation_chain = None
        self.vectorstore = None
        self.huggingface_token = os.getenv("HF_TOKEN")

    def load_document(self, pdf_file):
        """Carrega documento PDF de forma segura"""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(pdf_file.getvalue())
                tmp_file_path = tmp_file.name
            
            loader = PyPDFLoader(tmp_file_path)
            documents = loader.load()
            
            os.unlink(tmp_file_path)
            return documents
        except Exception as e:
            st.error(f"Erro ao carregar documento: {e}")
            return None

    def process_document(self, documents):
        """Processa documentos em chunks vetorizáveis"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
        splits = text_splitter.split_documents(documents)
        
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        self.vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        
        return self.vectorstore

    def create_conversation_chain(self):
        """Cria cadeia de conversação"""
        if not self.huggingface_token:
            st.error("Token da Hugging Face não configurado")
            return None

        llm = HuggingFaceEndpoint(
            endpoint_url="https://api-inference.huggingface.co/models/Qwen/Qwen2.5-3B-Instruct",
            huggingfacehub_api_token=self.huggingface_token,
            max_length=1024,
            temperature=0.7,
            max_new_tokens=1024
        )
        
        prompt_template = PromptTemplate.from_template("""
        Baseie-se estritamente no contexto fornecido para responder a pergunta.
        Se a resposta não estiver no contexto, indique que não possui informações suficientes.
    
        INSTRUÇÕES IMPORTANTES:
        - Forneça uma resposta COMPLETA e DETALHADA
        - NÃO INTERROMPA a resposta no meio
        - Se necessário, use parágrafos adicionais para explicar completamente
        - Garanta que a explicação seja clara e abrangente

        Contexto: {context}
        Pergunta: {question}

        Resposta completa e detalhada:
    """)
        
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        
        self.conversation_chain = (
            {"context": retriever, "question": RunnablePassthrough()} 
            | prompt_template 
            | llm 
            | StrOutputParser()
        )
        
        return self.conversation_chain

    def chat(self, question):
        """Realiza chat com o modelo"""
        if not self.conversation_chain:
            st.warning("Por favor, carregue um documento primeiro.")
            return None
        
        try:
            response = self.conversation_chain.invoke(question)
            return response
        except Exception as e:
            st.error(f"Erro durante a conversa: {e}")
            return None

def main():
    st.set_page_config(
        page_title="Simple_bot: Converse com seu PDF",
        page_icon="📄",
        layout="wide"
    )
    
    st.markdown("""
    <style>
    .main-title { 
        font-size: 2.5em; 
        color: #2c3e50; 
        text-align: center; 
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">Simple_bot: Converse com seu PDF 📄</h1>', unsafe_allow_html=True)
    
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = RAGChatbot()
    
    with st.sidebar:
        st.header("📄 Carregue seu PDF")
        
        pdf_file = st.file_uploader(
            "Selecione um documento PDF", 
            type=["pdf"]
        )
        
        if pdf_file:
            with st.spinner("Processando documento..."):
                documents = st.session_state.chatbot.load_document(pdf_file)
                
                if documents:
                    st.session_state.chatbot.process_document(documents)
                    st.session_state.chatbot.create_conversation_chain()
                    st.success("Documento processado!")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Faça uma pergunta sobre o documento"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.session_state.chatbot.chat(prompt)
            st.markdown(response)

        if response:
            st.session_state.messages.append({"role": "assistant", "content": response})

    st.markdown('<div style="text-align:center; margin-top:20px;">Desenvolvido por TheuxSR</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()