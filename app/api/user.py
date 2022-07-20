from fastapi import APIRouter
from app.settings import settings

router = APIRouter()


@router.get("/")
async def index():
    return {'hello': settings.postgre_url}
