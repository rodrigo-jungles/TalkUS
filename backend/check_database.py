#!/usr/bin/env python3
"""
Script para verificar dados no banco MySQL
"""
import mysql.connector
from database import engine
from sqlalchemy import text

print('🔍 Verificando configuração do banco de dados...')
print('📊 String de conexão: mysql+mysqlconnector://root:@localhost:3306/talkus')
print()

try:
    # Conectar diretamente ao MySQL para listar bancos
    print('🔌 Conectando ao MySQL...')
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = conn.cursor()
    
    # Listar todos os bancos de dados
    cursor.execute('SHOW DATABASES')
    databases = [db[0] for db in cursor.fetchall()]
    print('📋 Bancos de dados disponíveis:')
    for db in databases:
        print(f'   - {db}')
    
    if 'talkus' in databases:
        print('\n✅ Banco talkus encontrado!')
        
        # Conectar ao banco talkus
        cursor.execute('USE talkus')
        
        # Listar tabelas
        cursor.execute('SHOW TABLES')
        tables = [table[0] for table in cursor.fetchall()]
        print('📊 Tabelas no banco talkus:')
        for table in tables:
            print(f'   - {table}')
            
        if 'usuarios' in tables:
            print('\n👥 Dados na tabela usuarios:')
            cursor.execute('SELECT id, nome, email FROM usuarios')
            users = cursor.fetchall()
            if users:
                for user in users:
                    print(f'   ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}')
                    
                print(f'\n📊 Total de usuários: {len(users)}')
            else:
                print('   ❌ Nenhum usuário encontrado')
        else:
            print('\n❌ Tabela usuarios não encontrada')
    else:
        print('\n❌ Banco talkus não encontrado!')
        print('💡 Criando o banco...')
        
        cursor.execute('CREATE DATABASE talkus')
        print('✅ Banco talkus criado!')
    
    cursor.close()
    conn.close()
    
    print('\n' + '='*50)
    print('🔧 INSTRUÇÕES PARA O MYSQL WORKBENCH:')
    print('='*50)
    print('1. Abra o MySQL Workbench')
    print('2. Conecte com:')
    print('   - Host: localhost')
    print('   - Port: 3306') 
    print('   - Username: root')
    print('   - Password: (deixe em branco)')
    print('3. Procure pelo banco: TalkUS')
    print('4. Navegue até: TalkUS > Tables > usuarios')
    print('5. Clique com botão direito na tabela usuarios')
    print('6. Selecione "Select Rows - Limit 1000"')
    print('='*50)
    
except Exception as e:
    print(f'❌ Erro: {e}')
    
    print('\n💡 POSSÍVEIS PROBLEMAS:')
    print('1. MySQL não está rodando')
    print('2. Senha do root está diferente') 
    print('3. MySQL está em porta diferente de 3306')
    print('4. Banco TalkUS não foi criado')
    
    print('\n🔧 SOLUÇÕES:')
    print('1. Inicie o MySQL no XAMPP/WAMP')
    print('2. Verifique se o usuário root não tem senha')
    print('3. Tente conectar primeiro no Workbench manualmente')
