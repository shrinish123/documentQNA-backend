import databases 
import sqlalchemy
from api.config import config

metadata = sqlalchemy.MetaData()

document_table = sqlalchemy.Table(
    "documents",
    metadata, 
    sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column('title',sqlalchemy.String),
    sqlalchemy.Column('path', sqlalchemy.String,unique=True)
)

chat_message_table = sqlalchemy.Table(
    "chat_messages",
    metadata,
    sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column('document_id',sqlalchemy.ForeignKey("documents.id")),
    sqlalchemy.Column('sender',sqlalchemy.String),
    sqlalchemy.Column('content',sqlalchemy.String)
)

engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args = {"check_same_thread" : False}
)

metadata.create_all(engine)
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)