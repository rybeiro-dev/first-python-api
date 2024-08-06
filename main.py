import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Primeira API")

@app.get("/")
def index():
    return {"message": "Minha primeira Api"}

@app.get("/hello/{nome}")
def hello(nome):
    return f"Olá {nome}"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)


