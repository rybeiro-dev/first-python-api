from pydantic import BaseModel


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str


class UsuarioRequest(BaseModel):
    nome: str
    email: str
