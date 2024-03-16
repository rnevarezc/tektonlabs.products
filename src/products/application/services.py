from kink import inject

from src.products.application.dtos import ProductInDTO, ProductDTO
from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId
from src.products.domain.repositories import ProductRepository
from src.products.domain.errors import ProductNotFoundError

@inject
class ProductService:
    
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    async def get_by_id(self, product_id: str) -> ProductDTO:
        product = await self.repository.get(ProductId.of(product_id))

        if not product:
            raise ProductNotFoundError

        return ProductDTO(**product.dict())
    
    async def create_product(self, data: ProductInDTO) -> ProductDTO:
        product = Product.create(**data.dict())
        await self.repository.save(product)
        return ProductDTO(**product.dict())
    
    async def update_discount(self, product_id: str) -> ProductDTO:
        pass