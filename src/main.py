from fastapi import FastAPI
from src.modules.usuario.user_router import router as user_router


app = FastAPI()

app.include_router(user_router)


@app.get("/")
def ler_raiz():
    return {"Hello user": " E-commerce API Rodando"}
