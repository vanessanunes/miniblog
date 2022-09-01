
## Requesitos

- Python 3.10
- SQLAlchemy
- Alembic
- Docker Compose

## Configurações iniciais

Para instalar as dependencias, primeiro, crie uma ambiente de desenvolvimento e rode o seguinte comando:

`pip install -r requirements.txt`


Para criar as tabelas do banco rode:

```
alembic revision --autogenerate -m "create tables"

alembic upgrade head
```

Se você precisa mudar alguma coisa no banco de dados, mude o arquivo `data_definition.py` e depois rode:

```
alembic run migration_revision "escreva aqui seu comentário"

alembic upgrade head
```

Se precisar refazer alguma alteração no banco, rode (e não se esquece de deletar o arquivo que foi gerado para sua ultima migration, se isso for necessário)

```
alembic downgrade -1
```

## Rodar

### Unicorn

Para rodar localmente você pode optar por algum desses dois comandos:

`uvicorn "app.main:app" --reload` or `make run`

### Docker

Também temos a opção para Docker, e assim você pode executar algum desses comandos:

`docker-compose up -d` or `make run-docker`


<!---

api -> 
arquivo ou pasta models -> models as tabelinhas

arquivo routers.py
arquivo 


desgin pattern factory -> banco de dados / manipulação de dados


main.py -> chamar as routers
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter



https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi


--->
