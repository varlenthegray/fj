import time
from pathlib import Path
from fastapi import FastAPI, APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app import crud
from app.api import deps
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title="Faded Journals - API", openapi_url=f"{settings.API_V1_STR}/openapi.json")


@root_router.get("/", status_code=200, summary="A generic successful response.")
def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
    """
    Root GET
    """
    response = {"message": "You have successfully connected."}
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
