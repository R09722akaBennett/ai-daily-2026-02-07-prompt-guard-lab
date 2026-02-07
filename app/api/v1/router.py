from fastapi import APIRouter

from app.api.v1.routes import health
from app.api.v1.routes import guard

api_router = APIRouter()
api_router.include_router(health.router, tags=['health'])
api_router.include_router(guard.router, tags=['guard'])
