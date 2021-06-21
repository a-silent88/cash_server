from fastapi import APIRouter
from orm_db import session, Cash, engine, Incas
from datetime import datetime, timedelta
from sqlalchemy import desc

statistic = APIRouter()

currently = datetime.now()
today = datetime(currently.year, currently.month, currently.day, 0, 0, 0)


@statistic.get("/today/")
async def get_data():
    answer = session.query(Cash.amount).filter(Cash.time > today).all()[0]
    result = 0
    for i in answer:
        result += i
    return result


@statistic.get("/yesterday/")
async def get_data():
    answer = session.query(Cash.amount).filter((Cash.time > (today - timedelta(days=1))) & (Cash.time < today)).all()[0]
    result = 0
    for i in answer:
        result += i
    return result


@statistic.get("/week/")
async def get_data():
    answer = session.query(Cash.amount).filter(Cash.time > (today - timedelta(days=7))).all()[0]
    result = 0
    for i in answer:
        result += i
    return result


last_month = datetime(currently.year, (currently.month - 1), 1, 0, 0, 0)
current_month = datetime(currently.year, currently.month, 1, 0, 0, 0)


@statistic.get("/last_month/")
async def get_data():
    answer = session.query(Cash.amount).filter((Cash.time > last_month) & (Cash.time < current_month)).all()[0]
    result = 0
    for i in answer:
        result += i
    return result


@statistic.get("/current_month/")
async def get_data():
    answer = session.query(Cash.amount).filter(Cash.time > current_month).all()[0]
    result = 0
    for i in answer:
        result += i
    return result


@statistic.get("/after_incas/")
async def get_amount_after_incas(terminal_id: str = False):
    """
        Возвращаем сумму средств с последней инкассации
    """
    # if terminal_id:  # выборка по терминалу
    #     incas_time = session.query(Incas.time).order_by(desc(Incas.time)).filter(Incas.terminal == terminal_id).first()[0]
    #     cash_amount = session.query(Cash.amount).filter(Cash.time > incas_time).all()
    #     result = 0
    #     for i in cash_amount:
    #         result += i["amount"]
    #     print(result)
    #     return {"total amount in terminal": result}
    # else:
    #     ans = session.query(Incas.time).order_by(desc(Incas.time)).limit(1)
    #     print(ans[0])
    return {"in development"}
