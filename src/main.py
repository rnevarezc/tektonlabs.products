from fastapi import FastAPI

from src.common.db import database, engine, metadata
from src.products.routes import products

app = FastAPI(
    title ="Tektonlabs Products Microservice",
    description = "A small challenge from Tektonlabs of a products microservice",
    version="1.0.0",
)

@app.on_event("startup")
async def startup():
    await database.connect()

# This will create the DB schema and trigger the "after_create" event
# @app.on_event("startup")
# def configure():
#     metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def index():
    return {
        'title': "This is the products microservice",
        'version': '1.0.0'
    }

app.include_router(products)