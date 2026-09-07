from src.core.database import Base, engine, SessionLocal
from src.modules.usuario import UsuarioModel
from src.modules.clientes import ClienteModel
from src.modules.vendedor import VendedorModel


def test_mapeamento():

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        novo_usuario = UsuarioModel (
            email="dev.bruno@example.com",
            senha="hash_senha_segura",
        )

        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        print(f"✅ Usuário criado com ID: {novo_usuario.id_usuario}")


        novo_cliente = ClienteModel(
            id_usuario=novo_usuario.id_usuario,
            nome="Bruno Rodrigues",
            cpf="12345678901",
            sexo="M",
            data_nascimento="1998-01-01"
        )
        db.add(novo_cliente)
        db.commit()


        novo_vendedor = VendedorModel(
            id_usuario=novo_usuario.id_usuario,
            nome_loja="Tech Store Express",
            cnpj="12345678000199"
        )
        db.add(novo_vendedor)
        db.commit()


        user_db = db.query(UsuarioModel).filter_by(email="dev.bruno@example.com").first()

        print("\n--- Validação do Relacionamento ---")
        print(f"Nome do Cliente via Usuario: {user_db.profile_cliente.nome}")
        print(f"Nome da Loja via Usuario: {user_db.profile_vendedor.nome_loja}")
        print(f"Email via Cliente: {user_db.profile_cliente.usuario.email}")

    except Exception as e:
        print(f"❌ Erro de Mapeamento/Execução: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_mapeamento()