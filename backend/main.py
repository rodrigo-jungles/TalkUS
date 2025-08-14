# backend/main.py

from fastapi import FastAPI
import models
from database import engine

# Esta linha de código diz ao SQLAlchemy para criar todas as tabelas
# que ele encontrar nos modelos (que herdam de Base) no banco de dados.
# O `bind=engine` diz qual motor de banco de dados usar.
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá Mundo, a conexão com o banco de dados está pronta!"}


@app.get("/status")
def read_status():
    return {"status": "servidor online"}