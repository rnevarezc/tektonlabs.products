from kink import inject

from src.products.application.dtos import ProductInDTO, ProductDTO
from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId, Discount
from src.products.domain.repositories import ProductRepository
from src.products.domain.services import DiscountFetcher

@inject
class ProductService:
    
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    async def get_by_id(self, product_id: str) -> ProductDTO:
        product = await self.repository.get(ProductId.of(product_id))
        return ProductDTO(**product.model_dump())
    
    async def create_product(self, request: ProductInDTO) -> ProductDTO:
        product = Product.create(**request.model_dump())
        await self.repository.create(product)
        return ProductDTO(**product.model_dump())
    
    async def update_product(
        self, product_id: str, request: ProductInDTO
    ) -> ProductDTO:    
        product = await self.repository.get(ProductId.of(product_id))
        product.update(**request.model_dump())
        await self.repository.save(product)
        return ProductDTO(**product.model_dump())
    
    async def fetch_product_discount(
        self, product_id: str, discount_fetcher: DiscountFetcher
    ) -> Discount | None:
        return await discount_fetcher.fetch(product_id=product_id)

    async def update_product_discount(
        self, product_id: str, discount_fetcher: DiscountFetcher
    ) -> ProductDTO | None:

        product = await self.repository.get(ProductId.of(product_id))
        discount = await self.fetch_product_discount(
            product_id, discount_fetcher
        )
        
        if discount:
            product.update_discount(discount.get())
            await self.repository.save(product)
            return ProductDTO(**product.model_dump())
        
        return None