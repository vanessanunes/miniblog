from fastapi import FastAPI

from .api import user

app = FastAPI()


# iniciar as coneções com o db
app.include_router(user.router)
