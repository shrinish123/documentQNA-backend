from fastapi import APIRouter, HTTPException
from api.models.chat_message import ChatMessage,Question
from api.database import database,document_table,chat_message_table
from engine.main import get_answer
from engine.utils import get_chat_history

router = APIRouter(prefix='/chat_message')

async def append_new_qa(question:str, answer:str, doc_id:int) :
      
      ques_dict = {"document_id":doc_id,"sender":'Human', "content": question}
      query = chat_message_table.insert().values(ques_dict)
      await database.execute(query)
      
      ans_dict = {"document_id":doc_id,"sender":'AI', "content": answer}
      query =  chat_message_table.insert().values(ans_dict)
      await database.execute(query)
      

@router.post('/get_answer/{doc_id}', response_model = str)
async def get_chat_answer(doc_id : int,question : Question):
      
      
      query_doc = document_table.select().where(document_table.c.id == doc_id)
      doc = await database.fetch_one(query_doc)
      
      if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
      
      ## this can be replaced by sending the chat history from the frontend        
      chat_history_query = chat_message_table.select().where(chat_message_table.c.document_id == doc_id)
      chat_history_messages = await database.fetch_all(chat_history_query)
      
      chat_history = []
      get_chat_history(chat_history,chat_history_messages)
      
      # get the answer from the engine with Langchain 
      answer = get_answer(chat_history,question.question,doc.path)
      
      # Add the new qna to the chat table 
      await append_new_qa(question.question,answer.content,doc_id)
      
      return answer.content



  
@router.get('/getByDocId/{doc_id}', response_model=list[ChatMessage])
async def get_chat_messages_by_docId(doc_id:int):
      query = chat_message_table.select().where(chat_message_table.c.document_id == doc_id)
      return await database.fetch_all(query)

  