from enum import Enum
from typing import Optional, Any
from pydantic import BaseModel, Field, ValidationError, validator, model_serializer
from nanoid import generate

from src.products.domain.errors import (
    InvalidPriceError, ProductError, InvalidDiscountError
)

NANO_ID_LENGTH = 10

class ValueObject(BaseModel):
    """A base class for value objects"""
    value: Any

    @model_serializer
    def serialize(self):
        """ Default serialization
        By default a Value Object should be
        serialized into its own value and not 
        treated as a dict
        """
        return self.value

    def __str__(self) -> str:
        return str(self.value)
    
    def get(self):
        return self.value

class ProductId(ValueObject):
    value: str

    @classmethod
    def new(cls) -> "ProductId":
        return cls(value = generate(size=NANO_ID_LENGTH))
    
    @classmethod
    def validate(cls, val: str) -> str:
        val = val.strip()
        assert len(val) == NANO_ID_LENGTH, f"length must be {NANO_ID_LENGTH}"
        assert val.isalnum(), "must be alphanumeric"
        return val

    @classmethod
    def of(cls, id: str) -> "ProductId":
        try:
            return cls(value=cls.validate(id))
        except:
            raise ProductError.invalid_id()
        
class Discount(ValueObject):
    value: int = Field(frozen=True)

    @validator("value")
    def validate(cls, value):
        # A Discount should not be 100% or negative.
        if value >= 100 or value <=0:
            raise InvalidDiscountError        
        return value

class Price(ValueObject):
    value: float = Field(gt=0, frozen=True)
    
    def add_discount(self, discount: Discount):
        # Add a discount and return the new price.
        # (VOs are immutable by definition)
        new_price = self.value * (100 - discount.get())/100
        return Price(value=new_price)

class Status(Enum):
    Active = 1
    Inactive = 0
