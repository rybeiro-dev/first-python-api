from fastapi import APIRouter
from typing import List
from controllers.usuario_controller import UsuarioResponse, UsuarioRequest

router = APIRouter()


@router.get("/usuarios", response_model=List[UsuarioResponse])
def index():
    return [
        UsuarioResponse(
            id=1,
            nome='Teste',
            email='test3@email.com'
        )
    ]


@router.post('/', response_model=UsuarioResponse, status_code=201)
def create(user: UsuarioRequest):
    return UsuarioResponse(
        id=2,
        nome=user.nome,
        email=user.email
    )
