from datetime import datetime
from pydantic import BaseModel

from src.products.domain.errors import ProductError
from src.products.domain.value_objects import (
    Status as BaseStatus, 
    Price as BasePrice, 
    ProductId as BaseProductId,
    Discount as BaseDiscount
)

class Product(BaseModel):  
    ProductId: BaseProductId
    Name: str
    Status: bool
    Stock: int
    Description: str
    Price: BasePrice
    Discount: int | None = None
    FinalPrice: BasePrice | None = None
    CreatedAt: datetime | None = None
    UpdatedAt: datetime | None = None

    @classmethod
    def create(
        cls, Name: str, Status: int, Stock: int, Description: str, Price: float
    ) -> "Product":
        return cls(
            ProductId = BaseProductId.new(), 
            Name=Name, 
            Status=Status, 
            Stock=Stock, 
            Description=Description, 
            Price = BasePrice(value=Price),
            CreatedAt = datetime.now(),
        )
    
    @classmethod
    def make(
        cls, 
        ProductId: str, 
        Name: str, 
        Status: bool, 
        Stock: int, 
        Description: str, 
        Price: float,
        Discount: int = None,
        FinalPrice: float = None,
        CreatedAt: datetime = None,
        UpdatedAt: datetime = None
    )-> "Product":        
        return cls(
            ProductId = BaseProductId.of(ProductId), 
            Name=Name, 
            Status=Status, 
            Stock=Stock, 
            Description=Description, 
            Price = BasePrice(value=Price)
        )

    def update_discount(self, discount: int):
        self.Discount = BaseDiscount(value=discount)
        self.FinalPrice = self.Price.add_discount(self.Discount)
        self.touch()

    def touch(self):
        self.UpdatedAt = datetime.now()