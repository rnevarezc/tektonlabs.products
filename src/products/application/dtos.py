from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Status(str, Enum):
    Active = 'Active'
    Inactive = 'Inactive'

class BaseProduct(BaseModel):
    ProductId: str

class ProductInDTO(BaseModel):
    Name: str
    StatusName: Status
    Stock: int
    Description: str
    Price: float

class ProductDTO(ProductInDTO, BaseProduct):
    Discount: Optional[int] = None
    FinalPrice: Optional[float] = None