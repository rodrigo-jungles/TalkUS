# backend/models.py

from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    senha_hash = Column(String(255))