from os import getenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = "local"
    # database_string = f"postgresql://{getenv("POSTGRES_USER")}:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_HOST")}/{getenv("POSTGRES_DB")}"

    @property
    def postgre_url(self) -> str:
        return "postgresql://" + str(
            getenv("POSTGRES_USER")
        ) + ":" + str(
            getenv("POSTGRES_PASSWORD")
        ) + "@" + str(
            getenv("POSTGRES_HOST")
        ) + "/" + str(
            getenv("POSTGRES_DB")
        )

settings = Settings()