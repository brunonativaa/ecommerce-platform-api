from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True, future=True)


with engine.connect() as conexao:
    print("Conectado com sucesso")

Base = declarative_base()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)


Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield
    finally:
        db.close()
