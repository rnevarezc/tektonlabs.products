from abc import ABC, abstractmethod

from src.products.domain.value_objects import ProductId, Discount


class DiscountFetcher(ABC):

    @abstractmethod
    async def fetch(self, product_id: ProductId) -> Discount:
        pass