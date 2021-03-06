import psycopg2
from psycopg2 import sql
# from config import db_con
from fastapi import APIRouter
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASSWORD
import datetime
import pytz
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from orm_db import engine, session, Incas, Cash, con


incas = APIRouter()


# суммируем все записи в таблице cash по постам c момента последней записи об инкассации.
# Если записи об инкассации нет, берёт все записи о платежах по постам.
@incas.get("/after/")
async def get_after_incas():
    query = sql.SQL("SELECT DISTINCT terminal FROM public.cash ORDER BY terminal")
    cursor = con.cursor()
    cursor.execute(query)
    amount_sum = 0
    result = dict()
    print("ans:")
    for ans in cursor.fetchall():
        query = sql.SQL("SELECT time FROM public.incas WHERE terminal=%s ORDER BY time DESC LIMIT 1")
        cursor.execute(query, [ans[0]])
        d_time = cursor.fetchone()
        if d_time is not None:
            query = sql.SQL("SELECT sum(amount) FROM public.cash WHERE (time>%s and terminal=%s)")
            cursor.execute(query, [d_time[0], ans[0]])
            res = cursor.fetchone()
        else:
            query = sql.SQL("SELECT sum(amount) FROM public.cash WHERE terminal=%s")
            cursor.execute(query, [ans[0]])
            res = cursor.fetchone()
        amount_sum += int(res[0])
        result.update(dict.fromkeys([ans[0].strip()], (res[0] / 100)))
    result.update({"amount": (amount_sum / 100)})
    cursor.close()
    con.close()
    return result


class ItemAdd(BaseModel):
    terminals: str
    user_id: Optional[str] = None


# запись в базу времени инкассации. Передаётся список с номерами терминалов и пользователь. Для каждого
# терминала создаётся отдельная запись
# async def incas_f(terminal: list, user: str):
@incas.post("/add/")
async def incas_f(item: ItemAdd):
    l_time = datetime.datetime.now()
    print(l_time)
    # con = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = con.cursor()
    term_list = item.terminals.split(sep=',')
    for term in term_list:
        query = sql.SQL("INSERT INTO public.incas (terminal, user_id, time) VALUES (%s, %s, %s)")
        cursor.execute(query, [term.strip(), item.user_id, l_time])
    con.commit()
    cursor.close()
    # con.close()
    return HTMLResponse("True", status_code=200)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@incas.post("/add_alchemy/")
async def add_alchemy(item: ItemAdd):
    term_list = item.terminals.split(sep=',')
    for term in term_list:
        add_incas = Incas(terminal=term.strip(), user_id=item.user_id)
        session.add(add_incas)
        session.commit()
    return HTMLResponse(status_code=200)



