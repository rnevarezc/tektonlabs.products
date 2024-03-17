from kink import di

from src.products.domain.repositories import ProductRepository
from src.products.domain.services import DiscountFetcher
from src.products.infrastructure.repositories import MySQLProductRepository
from src.products.infrastructure.services import MockAPIDiscountFetcher
from src.products.application.services import ProductService
from src.common.db import database

def bootstrap_di() -> None:
    repository = MySQLProductRepository(database)
    discount_fetcher = MockAPIDiscountFetcher()

    di[ProductRepository] = repository
    di[DiscountFetcher] = discount_fetcher
    di[ProductService] = ProductService(repository)
    