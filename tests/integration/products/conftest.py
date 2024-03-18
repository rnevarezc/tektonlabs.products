import pytest
from kink import di

from src.products.application.services import ProductService
from src.products.domain.repositories import ProductRepository
from src.products.infrastructure.repositories import InMemoryProductRepository

@pytest.fixture()
def product_repository() -> ProductRepository:
    return InMemoryProductRepository()

@pytest.fixture()
def product_service(product_repository: ProductRepository) -> ProductService:
    return ProductService(product_repository)

@pytest.fixture()
def setup_di(product_service: ProductService) -> None:
    di[ProductService] = product_service