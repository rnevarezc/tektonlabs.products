from pydantic import BaseModel

class DomainError(Exception):
    pass

class ResourceNotFoundError(DomainError):
    pass

class APIErrorMessage(BaseModel):
    type: str
    message: str
