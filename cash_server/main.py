from fastapi import FastAPI
import uvicorn
from config import APP_PORT, APP_HOST
from pays import pay
from incas import incas
from statistic import statistic


app = FastAPI()

app.include_router(pay, prefix="/add_pay")
app.include_router(incas, prefix="/incas")
app.include_router(statistic, prefix="/statistic")


if __name__ == "__main__":
    uvicorn.run("main:app", host=APP_HOST, port=APP_PORT, log_level="debug")
