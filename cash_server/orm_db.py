from sqlalchemy import String, Table, Column, create_engine, MetaData, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy_utils import database_exists, create_database, drop_database
from config import db_str, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
import pytz
import psycopg2
from sqlalchemy.sql import func


engine = create_engine(db_str)
# если хотим очистить данные в таблицах при перезапуске
# if database_exists(engine.url):     # только от суперпользователя
#     drop_database(engine.url)
#     create_database(engine.url)

# создаём базу данных если она не существует
if not database_exists(engine.url):     # только от суперпользователя базы данных
    create_database(engine.url)


base = declarative_base()


class Cash(base):
    __tablename__ = 'cash'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)
    terminal = Column(String)
    coin = Column(Boolean)
    time = Column(DateTime(), server_default=func.now())


class Incas(base):
    __tablename__ = 'incas'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    terminal = Column(String)
    user_id = Column(String)
    time = Column(DateTime(), server_default=func.now(), default=func.now())


Session = sessionmaker(engine)
session = Session()
base.metadata.create_all(engine)


con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)
