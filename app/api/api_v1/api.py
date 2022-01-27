from fastapi import APIRouter
from app.api.api_v1.endpoints import recipe, author


api_router = APIRouter()
api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(author.router, prefix="/author", tags=["author"])
