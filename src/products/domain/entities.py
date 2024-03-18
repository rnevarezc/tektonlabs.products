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
    Status: BaseStatus
    Stock: int
    Description: str
    Price: BasePrice
    Discount: BaseDiscount | None = None
    FinalPrice: BasePrice | None = None
    CreatedAt: datetime | None = None
    UpdatedAt: datetime | None = None

    @classmethod
    def create(
        cls, Name: str, Status: BaseStatus, Stock: int, Description: str, Price: float
    ) -> "Product":     
        """ Factory method to create a Product from primitive data
        """
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
    def make(cls, **data)-> "Product":
        """ Factory method to make a Product instance from primitive data     
        """
        # Extract the primitives to convert to VO
        ProductId, Price, Discount, FinalPrice = map(
            data.get, (
                'ProductId', 'Price', 'Discount', 'FinalPrice'
            )
        )

        # Update the data dict.
        data.update({'ProductId': BaseProductId.of(ProductId)})
        data.update({'Price': BasePrice.of(Price)})
        data.update({'Discount': BaseDiscount.of(Discount) if Discount else None})
        data.update({'FinalPrice': BasePrice.of(FinalPrice) if FinalPrice else None})

        return cls(**data)

    def update_discount(self, discount: int):
        if discount:
            self.Discount = BaseDiscount.of(discount)
            self.FinalPrice = self.Price.add_discount(discount)
            self.touch()

    def update(self, **data) -> None:
        # Map Data Attributes
        Name, Status, Description, Stock, Price = map(
            data.get, (
                'Name', 'Status','Description', 'Stock', 'Price'
            )
        )
        self.Name = Name
        self.Status = Status
        self.Description = Description
        self.Stock = Stock
        self.Price = BasePrice.of(Price)

        if Price:
            self.update_discount(self.Discount)
        
        self.touch()

    def touch(self):
        self.UpdatedAt = datetime.now()

        