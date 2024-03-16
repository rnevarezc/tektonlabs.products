from fastapi import APIRouter, Depends, HTTPException
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

# @products.post("/products", status_code=201, response_model=ProductDTO)
# async def add_product(payload: ProductInDTO):    
#     product = await ProductRepository.save(payload)
#     return {**product.dict()}