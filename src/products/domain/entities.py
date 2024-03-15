from typing import Any, Optional
from dataclasses import dataclass

from src.products.domain.errors import ProductError
from src.products.domain.value_objects import Status, Price, ProductId

ProductSnapshot = dict[str, Any]

@dataclass
class Product:  
    ProductId: ProductId
    Name: str
    StatusName: Status
    Stock: int
    Description: str
    Price: Price
    Discount: Optional[int] = None
    FinalPrice: Optional[int] = None

    @classmethod
    def create(
        cls, ProductId: str, Name: str, StatusName: str, Stock: int, Description: str, Price: float
    ) -> "Product":
        return cls(ProductId.new(), Name, Status.Active, Stock, Stock, Description, Price(Price))
