from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse, Response
from kink import di

from src.products.application.dtos import ProductInDTO, ProductDTO
from src.products.application.services import ProductService
from src.common.errors import APIErrorMessage

products = APIRouter()

@products.get(
    "/products/{id}", 
    response_model=ProductDTO,
    responses={
        400: {"model": APIErrorMessage}, 
        404: {"model": APIErrorMessage}, 
        500: {"model": APIErrorMessage}
    },
)
async def get_product(id: str, service: ProductService = Depends(lambda: di[ProductService])):
    product = await service.get_by_id(id)
    return product

@products.post(
    "/products", 
    response_model=ProductDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": APIErrorMessage}, 
        500: {"model": APIErrorMessage}
    },
)
async def create_product(
    request: ProductInDTO, service: ProductService = Depends(lambda: di[ProductService])
):    
    product = await service.create_product(request)
    return product