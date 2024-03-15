from sqlalchemy import (Column, DateTime, Integer, MetaData, String, 
                        Table, Text, ARRAY, Enum, Float)

from src.common.db import metadata

# Products table
products = Table(
    'products',
    metadata,
    Column('ProductId', String(10), primary_key=True),
    Column('Name', String(256)),
    Column('StatusName', String(50)),
    Column('Stock', Integer),
    Column('Description', String(256)),
    Column('Price', Float),
    Column('FinalPrice', Float),
    Column('UpdatedAt', DateTime),
    Column('CreatedAt', DateTime)
)