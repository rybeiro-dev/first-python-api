# Primeiro passo
## Criar a Api com FastApi
O primeiro passo é criar um ambiente virtual para isolar a instalação de pacotes necessários para o aplicativo.

Sugiro o uso do Python na versão 3.9 ou superior.

```shell
python3 -m venv primeiro_app
```

Ativar o ambiente virtual.
```shell
# No Linux ou Unix
source primeiro_app/bin/activate
```

Para sair do ambiente virtual.
```shell
deactivate
```

## Instalar as dependências
Inicialmente vamos instalar os pacotes listados abaixo:
- `pip install uvicorn`
- `pip install fastapi`

Vamos criar o arquivo requirements.txt com as dependências do projeto.

Execute o comando a seguir:
```shell
python freeze >  requirements.txt
```

Esse arquivo será usado no deploy do aplicativo ou a execução em outro computador, com o seguinte comando:

```shell
pip install -r requirements.txt
```

# Segundo passo
Após criar o ambiente virtual e instalar as dependências é hora de criar os primeiros endpoints.

Criar o arquivo `main.py` esse script vai iniciar o servidor `uvicorn`  e o `fastapi`.

```python
# script main.py
import uvicorn
from fastapi import FastAPI

app = FastApi("Primeiro App")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

Iniciar o script com o comando `python main.py`

