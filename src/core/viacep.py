import httpx
from fastapi import HTTPException, status


async def buscar_endereco_por_cep(cep: str) -> dict:

    cep_limpo = cep.replace("-", "").replace(".", "").strip()

    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Formato de CEP inválido."
        )

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    async with httpx.AsyncClient() as cliente:
        try:
            response = await cliente.get(url, timeout=5.0)
            data = response.json()

            if data.get("erro") == "true" or response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="CEP não encontrado na base do ViaCEP."
                )

            return {
                "logradouro": data.get("logradouro", ""),
                "bairro": data.get("bairro", ""),
                "cidade": data.get("localidade", ""),
                "uf": data.get("uf", "")
            }

        except httpx.RequestError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Serviço de consulta de CEP indisponível no momento."
            )
