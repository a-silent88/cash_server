import datetime
import pytz
from fastapi import APIRouter
from cash_server.orm_db import session, Cash, engine, Incas
from datetime import datetime, timedelta
from sqlalchemy import desc
import sqlalchemy

# now = datetime.datetime.now(tz=pytz.timezone("Asia/Yekaterinburg"))
#
# print(now.strftime("%Y-%m-%d %H-%M-%S +05"))

terminal_id = 'barbusa_1'
# first()[0]
ans = session.query(Cash.terminal).distinct()
# term = {}
terminals_list = []
for i in ans:
    print(i["terminal"])
    amount_in_terminals = 0
    try:
        incas_time_t = session.query(Incas.time).order_by(desc(Incas.time)).filter(Incas.terminal == i["terminal"]).first()[0]
    except TypeError:  # Нет записи в базе данных
        print("запись об инкассации в терминале отсутствует")
        cash_amount_t = session.query(Cash.amount).filter(Cash.time > incas_time_t & Cash.terminal == i["terminal"]).all()
        # print("Сумма в терминале:", cash_amount_t)
        for j in cash_amount_t:
            amount_in_terminals += j["amount"]

        cash_amount_t = session.query(Cash.amount).filter(Cash.terminal == i["terminal"]).all()
        for j in cash_amount_t:
            amount_in_terminals += j["amount"]

print(amount_in_terminals)



