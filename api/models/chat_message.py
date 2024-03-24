from pydantic import BaseModel,ConfigDict

class ChatMessageIn(BaseModel):
    document_id : int 
    sender : str
    content : str

class ChatMessage(ChatMessageIn):
    model_config = ConfigDict(from_attributes = True)
    id : int
    
class Question(BaseModel):
    question: str




    
    