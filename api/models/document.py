from pydantic import BaseModel,ConfigDict
from api.models.chat_message import ChatMessage

class DocumentIn(BaseModel):
    title: str
    path : str

class Document(DocumentIn):
    model_config = ConfigDict(from_attributes = True)
    id : int

class DocumentWithChatHistory(BaseModel):
    document:Document
    chatHistory:list[ChatMessage]


    
    