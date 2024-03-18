import copy
from databases import Database

from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId
from src.products.domain.repositories import ProductRepository
from src.products.domain.errors import ProductNotFoundError
from src.products.infrastructure.schemas import products


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

    async def create(self, product: Product) -> None:
        query = (
            products
            .insert()
            .values(**product.dict())
        )
        return await self.db.execute(query=query)


class InMemoryProductRepository(ProductRepository):

    def __init__(self) -> None:
        self.products = dict = {}

    async def get(self, product_id: ProductId) -> Product:
        try:
            return copy.deepcopy(self.products[product_id])
        except KeyError as error:
            print (f"In repo: {product_id}")
            raise ProductNotFoundError(f"A record was not found with the '{product_id}' ID")

    async def save(self, product: Product) -> None:
        self.products[product.ProductId] = copy.deepcopy(product)

    async def create(self, product: Product) -> None:
        self.products[product.ProductId] = copy.deepcopy(product)