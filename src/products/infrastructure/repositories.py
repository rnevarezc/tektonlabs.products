from databases import Database

from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId
from src.products.domain.repositories import ProductRepository
from src.products.domain.errors import ProductNotFoundError
from src.products.infrastructure.schemas import products

import json

class MySQLProductRepository(ProductRepository):

    def __init__(self, db: Database) -> None:
        self.db = db

    async def get(self, product_id: ProductId) -> Product:
        query = (
            products
            .select()
            .where(products.c.ProductId==product_id)
        )
        record = await self.db.fetch_one(query=query)

        if not record:
            raise ProductNotFoundError(f"A record was not found with the '{product_id}' ID")
        
        return Product.make(**record)

    def get_all(self) -> list[Product]:
        pass

    async def save(self, product: Product) -> None:
        query = (
            products
            .update()
            .where(products.c.ProductId==product.ProductId)
            .values(**product.dict())
        )
        return await self.db.execute(query=query)