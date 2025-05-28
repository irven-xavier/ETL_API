from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Pega a url do db no .env
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Cria conexão com o db
engine = create_engine(DATABASE_URL)

# Cria uma sessão no db
Session = sessionmaker(bind=engine)

# Criação de uma base
Base = declarative_base()

# Define o modelo da tabela no db e cria as colunas
class tabela_vendas(Base):

    __tablename__ = "tabela_vendas"

    id = Column(String, primary_key=True)
    data = Column(DateTime)
    categoria = Column(String)
    valor = Column(Float)
    parcelas = Column(String(10))
    data_extracao = Column(DateTime)

# Gera a tabela de acordo com o Class
Base.metadata.create_all(engine)

