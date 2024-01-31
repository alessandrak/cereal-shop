from fastapi import Depends, FastAPI

from src.config.database import get_db
from src.core import routes

app = FastAPI()

app.include_router(routes.api_router, dependencies=[Depends(get_db)])
