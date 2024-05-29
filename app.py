import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import pickle
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered LangChain PDF Q&A bot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    st.write('Made with ❤️ by [Jobin Selvanose](https://www.linkedin.com/in/jobinselvanose/)')

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def main():
    st.header('Chat with your PDF 💬')

    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, length_function=len)
        chunks = text_splitter.split_text(text=text)
        store_name = pdf.name[:-4]
        

        if os.path.exists(f'{store_name}.pkl'):
            with open(f"./stores/{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"./stores/{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            
        query = st.text_input("Ask questions about your PDF!")


        if(query):
            docs = VectorStore.similarity_search(query=query, k=3)

            llm = ChatOpenAI(model_name='gpt-3.5-turbo')
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)

if __name__ == '__main__':
    main()