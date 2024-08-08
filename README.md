# Passo 1: Instalação, configuração e dependências
## Criar a Api com FastApi
O primeiro passo é criar um ambiente virtual para isolar a instalação de pacotes necessários para o aplicativo.

Sugiro o uso do Python na versão 3.9 ou superior.

```shell
python3 -m venv primeiro_app
```

Ativar o ambiente virtual.
```shell
# No Linux ou Unix, estando na raiz do projeto
source bin/activate
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

# Passo 2: script principal
Após criar o ambiente virtual e instalar as dependências é hora de criar os primeiros endpoints.

Criar o arquivo `main.py` esse script vai iniciar o servidor `uvicorn`  e o `fastapi`.

[visualizar o main.py](https://github.com/rybeiro-dev/first-python-api/blob/main/main.py)

Iniciar o script com o comando `python main.py`

# Passo 3: Estrutura MVC
Criar a estrutura de diretórios para a aplicação, na raiz do projeto, conforme segue:
- `test`
- `models`
- `controllers`
- `routes`
- `databases`

# Passo 4: Route
Criar a rota de acesso ao cadastro de usuários. No pacote `routes` criar o script usuario_router.py

Nas rotas vamos utilizar o módulo `ApiRouter` do pacote `fastapi`. 

[visualizar o usuario_router.py](https://github.com/rybeiro-dev/first-python-api/blob/main/routes/usuario_router.py)

# Passo 5: Controller
Criar a controller de Usuário para as devidas actions, index e create.

[visualizar o usuario_router.py](https://github.com/rybeiro-dev/first-python-api/blob/main/controllers/usuario_controller.py)

# Passo 6: Test
Para iniciar os teste instale o módulo `pytest` e crie o pacote `routes` dentro do pacote `test`. Dentro do pacote
routes crie o script `test_usuario.py`

[visualizar o script test_usuario.py]()

Execute o comando `pytest` no diretório root do projeto.

# Passo 7: Models
