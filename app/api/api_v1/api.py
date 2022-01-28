from fastapi import APIRouter
from app.api.api_v1.endpoints import author


api_router = APIRouter()
api_router.include_router(author.router, prefix="/author", tags=["author"])
