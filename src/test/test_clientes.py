from fastapi.testclient import TestClient
from src.api.main import app


client = TestClient(app)


def test_criar_cliente_com_cep_valido_sucesso():
    """
    Teste de Integração: Garante que um CEP válido consome o ViaCEP 
    e retorna status 201 com os dados de endereço enriquecidos.

    """
    payload = {
        "nome": "Cliente Teste",
        "email": "teste@exemplo.com",
        "cpf": "12345678901",
        "cep": "06857810",
        "numero": "50",
        "complemento": "Sala 1"
    }

    response = client.post("/clientes", json=payload)

    if response.status_code != 201:
        print("\n[DEBUG] RESPOSTA DA API:", response.json())

    assert response.status_code == 201
    data = response.json()
    assert data["mensagem"] == "Cliente e endereço inseridos com sucesso via ViaCEP!"
    assert data["dados"]["logradouro"] == "Estrada dos Guarantãs"
    assert data["dados"]["uf"] == "SP"


def test_criar_cliente_com_email_invalido_deve_falhar():
    """
    Teste de Borda: Garante que e-mails fora do padrão sintático 
    sejam rejeitados na camada de schema com HTTP 422.
    """
    payload = {
        "nome": "Cliente Invalido",
        "email": "email_sem_formato",
        "cpf": "11122233344",
        "cep": "06857810",
        "numero": "50"
    }

    response = client.post("/clientes", json=payload)
    assert response.status_code == 422
