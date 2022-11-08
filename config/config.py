import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# class Database:
#     def __init__(self, env):
#         load_dotenv(env + ".env")
#         username = os.getenv("USERNAME")
#         password = os.getenv("PASSWORD")
#         db_host = os.getenv("DB_HOST")
#         db_port = os.getenv("DB_PORT")
#         db = os.getenv("DB")
#         database_uri = f'postgresql://{username}:{password}@{db_host}:{db_port}/{db}'
#         print(database_uri)


database_uri = "postgresql://postgres:1234@localhost:5432/test_db4"

engine = create_engine(database_uri)


Session = sessionmaker(bind=engine)

Base = declarative_base()


# def set_environment(env):
#     load_dotenv(env + ".env")
#     username = os.getenv("USERNAME")
#     password = os.getenv("PASSWORD")
#     db_host = os.getenv("DB_HOST")
#     db_port = os.getenv("DB_PORT")
#     db = os.getenv("DB")
#     global DATABASE_URI
#     DATABASE_URI = f'postgresql://{username}:{password}@{db_host}:{db_port}/{db}'
#     print(DATABASE_URI)
