from pydantic import BaseModel, Field, computed_field
from typing import Optional
from src.products.domain.value_objects import Status as BaseStatus
from datetime import datetime

class BaseProduct(BaseModel):
    ProductId: str

class ProductInDTO(BaseModel):
    Name: str
    Status: BaseStatus = Field(serialization_alias='StatusName')
    Stock: int
    Description: str
    Price: float

class ProductDTO(ProductInDTO, BaseProduct):
    Discount: Optional[int] = None
    FinalPrice: Optional[float] = None
    CreatedAt: Optional[datetime] = None
    
    @computed_field
    def StatusName(self) -> str:
        return self.Status.name