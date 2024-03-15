from databases import Database

from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId
from src.products.domain.repositories import ProductRepository
from src.products.infrastructure.schemas import products

class MySQLProductRepository(ProductRepository):

    def __init__(self, db: Database) -> None:
        self.db = db
    
    async def get(self, product_id: ProductId) -> Product:
        query = (
            products.
            select().
            where(products.c.ProductId==product_id)
        )
        return await self.db.fetch_one(query=query)

    def get_all(self) -> list[Product]:
        pass

    def save(self, product: Product) -> None:
        pass