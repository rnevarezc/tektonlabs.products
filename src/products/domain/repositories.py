from abc import ABC, abstractmethod

from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId

class ProductRepository(ABC):
    
    @abstractmethod
    async def get(self, product_id: ProductId) -> Product:
        pass

    # @abstractmethod
    # async def get_all(self) -> list[Product]:
    #     pass

    @abstractmethod
    async def save(self, product: Product) -> None:
        pass

    @abstractmethod
    async def create(self, product: Product) -> None:
        pass