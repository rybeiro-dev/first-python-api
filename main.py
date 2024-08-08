import uvicorn
from fastapi import FastAPI
from routes import usuario_router

app = FastAPI(title="Primeira API")

app.include_router(usuario_router.router)


@app.get("/")
def index():
    return {"message": "Minha primeira Api"}


@app.get("/hello/{nome}")
def hello(nome):
    return f"Olá {nome}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True, workers=True)


