from sqlalchemy import String, Table, Column, create_engine, MetaData, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy_utils import database_exists, create_database
from config import db_str, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
import pytz
import psycopg2

engine = create_engine(db_str)

if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))
base = declarative_base()


class Cash(base):
    __tablename__ = 'cash'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)
    terminal = Column(String)
    coin = Column(Boolean)
    time = Column(DateTime, default=datetime.datetime.now(tz=pytz.timezone("Asia/Yekaterinburg")))


class Incas(base):
    __tablename__ = 'incas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    terminal = Column(String)
    user = Column(String)
    time = Column(DateTime, default=datetime.datetime.now(tz=pytz.timezone("Asia/Yekaterinburg")))


Session = sessionmaker(engine)
session = Session()

base.metadata.create_all(engine)


con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)
