# backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de Conexão com o Banco de Dados MySQL
# Formato: "mysql+mysqlconnector://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/TalkUS"

# Cria o "motor" de conexão do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma classe de Sessão que usaremos para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe Base da qual nossos modelos de dados (tabelas) irão herdar
Base = declarative_base()