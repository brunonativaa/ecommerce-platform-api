from fastapi import FastAPI
<<<<<<< HEAD
from src.modules.usuario.user_router import router as user_router
=======
from src.modules.clientes.router import router as clientes_router
>>>>>>> develop


app = FastAPI()

app.include_router(user_router)


@app.get("/")
def ler_raiz():
    return {"Hello user": " E-commerce API Rodando"}
