# backend/crud.py

from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

# Cria um contexto para hashing de senhas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email: str):
    """Busca um usuário pelo e-mail."""
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_user(db: Session, user: schemas.UsuarioCreate):
    """Cria um novo usuário no banco de dados."""
    hashed_password = get_password_hash(user.password)
    # Cria um objeto de modelo SQLAlchemy com os dados
    db_user = models.Usuario(
        email=user.email,
        nome=user.nome,
        senha_hash=hashed_password
    )
    db.add(db_user) # Adiciona o objeto à sessão
    db.commit() # Salva as mudanças no banco
    db.refresh(db_user) # Atualiza o objeto com os dados do banco (como o ID gerado)
    return db_user