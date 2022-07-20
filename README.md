
## Requirement
Python 3.10
SQLAlchemy
Alembic
Docker Compose

## Configuration
To install dependencies, first, create your virtual environment, run:
` pip install -r requirements.txt`

To run database configurations, run
```
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```

If need change something in the database, change file `data_definition.py` and after run:
```
pipenv run migration_revision "escreva aqui seu comentário"

alembic upgrade head

```

With nedded to undone things in database, run (and don't forget to delete the file generate from your last migration, with it's necessary):

```
alembic downgrade -1
```

## Run
To run local, run
`uvicorn "app.main:app" --reload`

Or
`make run`




api -> 
arquivo ou pasta models -> models as tabelinhas

arquivo routers.py
arquivo 


desgin pattern factory -> banco de dados / manipulação de dados


main.py -> chamar as routers
https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter



https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi



