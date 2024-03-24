from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager


from api.routers.document import router as document_router
from api.routers.chat_message import router as chat_message_router
from api.database import database

@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.connect()
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

# middlewares 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
# routers 
app.include_router(document_router)
app.include_router(chat_message_router)
