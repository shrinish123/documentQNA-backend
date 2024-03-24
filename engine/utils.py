from langchain_core.messages import AIMessage, HumanMessage
from api.models.chat_message import ChatMessage

def get_message(message : ChatMessage) : 
    
    if message.sender == 'AI':
        return AIMessage(content=message.content)
    else :
        return HumanMessage(content=message.content)


def get_chat_history(chat_history,chat_history_messages):
        
    for chat_history_message in chat_history_messages : 
        chat_history.append(get_message(chat_history_message))
        
    
    
    
