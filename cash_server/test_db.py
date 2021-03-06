import psycopg2
from psycopg2 import sql
from config import DB_HOST,DB_PORT, DB_USER, DB_NAME, DB_PASSWORD

l = ["15", "16"]
print(type(l))
req = {"terminal": l}
print(req)



