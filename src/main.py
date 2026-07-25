from fastapi import FastAPI
from src.modules.clientes.clientes_router import router as clientes_router


app = FastAPI()

app.include_router(clientes_router)


@app.get("/")
def ler_raiz():
    return {"Hello user": "API E-commerce Rodando"}
