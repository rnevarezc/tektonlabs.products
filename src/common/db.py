import os
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)

metadata = MetaData()

# Set the database instance
database = Database(DATABASE_URI)