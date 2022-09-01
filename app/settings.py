from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = "local"
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str

    @property
    def postgre_url(self) -> str:
        """Create a databse url

        Returns:
            str: database url
        """
        return f"postgresql://{self.postgres_user}:" \
            f"{self.postgres_password}@{self.postgres_host}/{self.postgres_db}"

    class Config():
        env_file = '.env'


settings = Settings()
