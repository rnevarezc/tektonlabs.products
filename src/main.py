from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from src.common.db import database
from src.common.errors import APIErrorMessage, ResourceNotFoundError
from src.products.routes import products
from src.common.middlewares import RouterLoggingMiddleware

import logging
import src.common.logs

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(
    title ="Tektonlabs Products Microservice",
    description = "A small challenge from Tektonlabs of a products microservice",
    version="1.0.0",
    lifespan = lifespan
)

app.add_middleware(
    RouterLoggingMiddleware,
    logger=logging.getLogger(__name__)
)

# This will create the DB schema and trigger the "after_create" event
# @app.on_event("startup")
# def configure():
#     metadata.create_all(bind=engine)

@app.exception_handler(ResourceNotFoundError)
async def resource_not_found_handler(request: Request, exc: ResourceNotFoundError) -> JSONResponse:
    error_msg = APIErrorMessage(type=exc.__class__.__name__, message=str(exc))
    return JSONResponse(status_code=404, content=error_msg.dict())

# API main routes...
# -----------------------------------------------------------------------------
@app.get("/")
def index():
    return {
        'title': "This is the products microservice",
        'version': '1.0.0'
    }

app.include_router(products)
