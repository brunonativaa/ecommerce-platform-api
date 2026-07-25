from fastapi import APIRouter, status, HTTPException
from src.modules.clientes.clientes_schema import ClienteCreateInput
from src.core.viacep import buscar_endereco_por_cep


router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteCreateInput):

    dados_endereco = await buscar_endereco_por_cep(cliente.cep)

    novo_cliente_completo = {
        "nome": cliente.nome,
        "email": cliente.email,
        "cpf": cliente.cpf,
        "cep": cliente.cep,
        "numero": cliente.numero,
        "complemento": cliente.complemento,
        "logradouro": dados_endereco["logradouro"],
        "bairro": dados_endereco["bairro"],
        "cidade": dados_endereco["cidade"],
        "uf": dados_endereco["uf"]
    }

    return {
        "mensagem": "Cliente e endereço inseridos com sucesso via ViaCEP!",
        "dados": novo_cliente_completo
    }
