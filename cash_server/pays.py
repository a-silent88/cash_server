# from psycopg2 import sql
from fastapi import APIRouter
from orm_db import session, Cash, engine

pay = APIRouter()


@pay.get("/")
async def add_pay(amount_t: int = 0, terminal: str = '', coin: bool = False):
    if amount_t > 0 and terminal != '':
        add_terminal = Cash(amount=amount_t, terminal=terminal, coin=coin)
        session.add(add_terminal)
        session.commit()


# @pay.get("/")
# async def add_pay(amount_t: int = 0, terminal: str = '', coin: bool = False):
#     if amount_t > 0 and terminal != '':
#         query = sql.SQL("INSERT INTO cash.schema_name.cash (amount, coin, terminal_id)"
#                         " VALUES (%s, %s, %s)")
#
#         engine.execute(query, [amount_t, coin, terminal])
#         engine.commit()
#         return "True"
#     else:
#         return "False"
