from src.common.errors import DomainError, ResourceNotFoundError

class InvalidPriceError(DomainError):
    pass

class InvalidDiscountError(DomainError):
    pass

class ProductError(DomainError):
    
    @classmethod
    def invalid_id(cls) -> "ProductError":
        return cls("Provided id is not a valid ProductId")

class ProductNotFoundError(ResourceNotFoundError):
    pass

