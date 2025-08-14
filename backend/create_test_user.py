#!/usr/bin/env python3
import sys
sys.path.append('.')
from crud import create_user, get_user_by_email
from database import SessionLocal
import schemas

# Criar sessão do banco
db = SessionLocal()

try:
    # Verificar se usuário já existe
    existing_user = get_user_by_email(db, 'teste@test.com')
    
    if existing_user:
        print('ℹ️  Usuário já existe!')
        print(f'   Nome: {existing_user.nome}')
        print(f'   Email: {existing_user.email}')
    else:
        # Dados do usuário
        user_data = schemas.UsuarioCreate(
            nome='Usuario Teste',
            email='teste@test.com', 
            password='123456'
        )
        
        # Criar usuário
        new_user = create_user(db, user_data)
        print('✅ Usuário criado com sucesso!')
        print(f'   ID: {new_user.id}')
        print(f'   Nome: {new_user.nome}')
        print(f'   Email: {new_user.email}')
    
    print('')
    print('🔑 Use estas credenciais no login:')
    print('   Email: teste@test.com')
    print('   Senha: 123456')
    
except Exception as e:
    print(f'❌ Erro: {e}')
    import traceback
    traceback.print_exc()
finally:
    db.close()
