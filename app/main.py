from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
import os
from model import Base

DB_URL = os.getenv('DB_URL')


@asynccontextmanager
async def lifespan(api: FastAPI):
    api.state.eng = create_engine(DB_URL)
    Base.metadata.create_all(api.state.eng)
    print('таблицы созданы')
    yield
    api.state.eng.dispose()
    print('engine отключен')

api = FastAPI(lifespan=lifespan)

if __name__=='__main__':
    uvicorn.run(app='main:api', host='0.0.0.0', port=8000, reload=True)