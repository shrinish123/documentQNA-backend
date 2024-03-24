import os
from operator import itemgetter
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.prompts.prompt import PromptTemplate
from langchain_core.messages import get_buffer_string


load_dotenv()
doc_path = os.path.join(os.path.dirname(__file__), '..', 'docs/test2.pdf')


def load_docs(file_path):
  loader = PyMuPDFLoader(file_path)
  documents = loader.load()
  return documents

def split_docs(documents, chunk_size=1000, chunk_overlap=0):
  text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs


def get_answer(chat_history,question,doc_path):

    documents = load_docs(doc_path) 
    splitted_docs = split_docs(documents)
    
    embeddings = OpenAIEmbeddings()
    
    vectorstore = FAISS.from_documents(splitted_docs, embedding=embeddings)
    retriever = vectorstore.as_retriever()
    
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.

    Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:"""
    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)
    
    
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
    
    
    model = ChatOpenAI(temperature=0)
    
    
    _inputs = RunnableParallel(
    standalone_question=RunnablePassthrough.assign(
        chat_history=lambda x: get_buffer_string(x["chat_history"])
    )
    | CONDENSE_QUESTION_PROMPT
    | model
    | StrOutputParser(),
    )
    
    _context = {
        "context": itemgetter("standalone_question") | retriever,
        "question": lambda x: x["standalone_question"],
    }
    conversational_qa_chain = _inputs | _context | ANSWER_PROMPT | model


    response = conversational_qa_chain.invoke(
    {
        "question": question,
        "chat_history": chat_history
    })

    return response




