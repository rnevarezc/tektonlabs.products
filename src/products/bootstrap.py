from kink import di

from src.products.domain.repositories import ProductRepository
from src.products.infrastructure.repositories import MySQLProductRepository
from src.products.application.services import ProductService
from src.common.db import database

def bootstrap_di() -> None:
    repository = MySQLProductRepository(database)

    di[ProductRepository] = repository
    di[ProductService] = ProductService(repository)