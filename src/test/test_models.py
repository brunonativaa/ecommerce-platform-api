from datetime import date
from src.core.database import Base, engine, SessionLocal
from src.modules.usuario.user_model import UsuarioModel
from src.modules.clientes.cliente_model import ClienteModel

# 1. Cria as tabelas no banco (se ainda não existirem)
print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # 2. Instancia e salva um Novo Usuário
    novo_usuario = UsuarioModel(
        email="teste.relacionamento@email.com",
        senha="senha_criptografada_aqui"
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    print(f"✅ Usuário criado com sucesso! ID: {novo_usuario.id_usuario}")

    # 3. Instancia e salva o Cliente atrelado ao ID do Usuário criado
    novo_cliente = ClienteModel(
        id_usuario=novo_usuario.id_usuario,  # Usa a chave estrangeira (FK)
        nome="Bruno Teste ORM",
        cpf="12345678901",
        sexo="M",
        data_nascimento=date(1997, 8, 15)
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    print(f"✅ Cliente vinculado criado com sucesso! ID Cliente: {novo_cliente.id_cliente} | ID Usuário: {novo_cliente.id_usuario}")

except Exception as e:
    db.rollback()
    print(f"❌ Erro ao testar as models: {e}")
finally:
    db.close()