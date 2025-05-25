from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Pega a url do db no .env
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Cria o engine do db
engine = create_engine(DATABASE_URL)

# Cria uma sessão no db
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Define o nome da tabela no db e cria as colunas
class meu_db(Base):
    __tablename__ = "meu_db"

    id = Column(String, primary_key=True)
    data = Column(DateTime)
    categoria = Column(String)
    valor = Column(Float)
    parcelas = Column(String(10))
    data_extracao = Column(DateTime)

Base.metadata.create_all(engine)

