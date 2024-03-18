from fastapi import APIRouter, Depends, status, BackgroundTasks
from kink import di

from src.products.application.dtos import ProductInDTO, ProductDTO
from src.products.application.services import ProductService
from src.products.domain.services import DiscountFetcher
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
async def get_product(
    id: str, service: ProductService = Depends(lambda: di[ProductService])
) -> ProductDTO:
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
    request: ProductInDTO, 
    service: ProductService = Depends(lambda: di[ProductService]),
    tasks: BackgroundTasks = BackgroundTasks
) -> ProductDTO:    
    product = await service.create_product(request)

    # Handle the discount fetch and update in the background
    # This way the consumer doesnt have to wait a chained response.
    tasks.add_task(
        service.update_product_discount, 
        product.ProductId, 
        di[DiscountFetcher]
    )

    return product

@products.put(
    "/products/{id}",
    response_model=ProductDTO,
    responses={
        400: {"model": APIErrorMessage}, 
        404: {"model": APIErrorMessage}, 
        500: {"model": APIErrorMessage}
    }
)
async def update_product(
    id: str, request: ProductInDTO, service: ProductService = Depends(lambda: di[ProductService])
) -> ProductDTO:
    
    product = await service.update_product(id, request)
    return product