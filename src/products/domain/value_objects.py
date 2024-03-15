from enum import Enum
from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass
from nanoid import generate

from src.products.domain.errors import (
    InvalidPriceError, ProductError, InvalidDiscountError
)

NANO_ID_LENGTH = 10

class ValueObject:
  """A base class for all value objects"""

@dataclass(frozen=True)
class ProductId:
    value: str

    @classmethod
    def new(cls) -> "ProductId":
        return cls(generate(size=NANO_ID_LENGTH))
    
    @classmethod
    def validate(cls, val: str) -> str:
        val = val.strip()
        assert len(val) == NANO_ID_LENGTH, f"length must be {NANO_ID_LENGTH}"
        assert val.isalnum(), "must be alphanumeric"
        return val

    @classmethod
    def of(cls, id: str) -> "ProductId":
        try:
            return cls(cls.validate(id))
        except:
            raise ProductError.invalid_id()

    def __str__(self) -> str:
        return str(self.value)

@dataclass(frozen=True)
class Discount(ValueObject):
    value: int = None

    # A Discount should not be 100%.
    def __post_init__(self):
       if self.value >= 100:
          raise InvalidDiscountError         

@dataclass(frozen=True)
class Price(ValueObject):
    value: int = None
    
    def __post_init__(self):
       # Round 2 decimals.
       self.value = str(round(self.value, 2))
       
       # A price cant be negative.
       if self.value < 0:
          raise InvalidPriceError          

    # Add a discount and return the new price.
    def add_discount(self, discount: int):
       new_price = self.value * (100 - discount)/100
       return Price(new_price)

@dataclass
class Status(str, Enum):
    Active = '1'
    Inactive = '0'
