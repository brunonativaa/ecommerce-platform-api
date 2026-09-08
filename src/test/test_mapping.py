import uuid
import random
from src.core.database import Base, SessionLocal, engine
from src.modules.clientes.model import ClienteModel
from src.modules.usuario.model import UsuarioModel
from src.modules.vendedor.model import VendedorModel


cpf_teste = f"{random.randint(10000000000, 99999999999)}"

def testar_mapeamento():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 1. Gera identificadores únicos para evitar UniqueViolation
        uid = uuid.uuid4().hex[:8]

        novo_usuario = UsuarioModel(
            email=f"dev.bruno_{uid}@example.com", senha="hash_senha_segura"
        )
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        # 2. Cria Cliente associado ao ID do usuário
        novo_cliente = ClienteModel(
            id_usuario=novo_usuario.id_usuario,
            nome="Bruno Rodrigues",
            cpf=cpf_teste,  # Garante CPF único para o teste
            sexo="M",
            data_nascimento="1998-01-01",
        )
        db.add(novo_cliente)

        # 3. Cria Vendedor associado
        novo_vendedor = VendedorModel(
            id_usuario=novo_usuario.id_usuario,
            nome_loja=f"Loja Tech {uid}",
            cnpj=f"{uid[:14]}",  # Garante CNPJ único
        )
        db.add(novo_vendedor)

        # Commit de ambas as entidades associadas
        db.commit()

        # 4. Força recarregamento do objeto a partir do banco
        db.expire_all()
        user_db = (
            db.query(UsuarioModel)
            .filter_by(id_usuario=novo_usuario.id_usuario)
            .first()
        )

        print("\n--- Validação do Relacionamento ---")
        print(f"✅ Nome do Cliente via Usuario: {user_db.profile_cliente.nome}")
        print(
            f"✅ Nome da Loja via Usuario: {user_db.profile_vendedor.nome_loja}"
        )
        print(f"✅ Email via Cliente: {user_db.profile_cliente.usuario.email}")

    except Exception as e:
        db.rollback()
        print(f"❌ Erro de Mapeamento/Execução: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    testar_mapeamento()