# backend/schemas.py

from pydantic import BaseModel

# Schema para a criação de um usuário (o que o cliente envia)
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    password: str  # Note que aqui pedimos a senha em texto puro

# Schema para a leitura de um usuário (o que a API retorna)
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True  # Permite que o Pydantic leia dados de objetos ORM (SQLAlchemy)

# Schema para o token de acesso
class Token(BaseModel):
    access_token: str
    token_type: str
