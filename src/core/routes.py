from fastapi import APIRouter

from src.items.routes import items_router

api_router = APIRouter(prefix="/api")

api_router.include_router(items_router)
