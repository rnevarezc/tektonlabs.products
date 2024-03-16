from sqlalchemy import (Column, DateTime, Integer, MetaData, String, 
                        Table, Text, ARRAY, Enum, Float, Boolean)

from src.common.db import metadata

# Products table
products = Table(
    'products',
    metadata,
    Column('ProductId', String(10), primary_key=True),
    Column('Name', String(256)),
    Column('Status', Integer),
    Column('Stock', Integer),
    Column('Description', String(256)),
    Column('Price', Float),
    Column('Discount', Integer),
    Column('FinalPrice', Float),
    Column('UpdatedAt', DateTime),
    Column('CreatedAt', DateTime)
)