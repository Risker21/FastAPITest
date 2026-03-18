from datetime import datetime

from fastapi import FastAPI
from sqlalchemy import DateTime, func, Integer, String, Float
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from 创建分路由.test import test
from 创建分路由.test2 import test2
from 请求体传参.test3 import test3
from 路由传参.test1 import test1

app = FastAPI()

app.include_router(test)
app.include_router(test1)
app.include_router(test2)
app.include_router(test3)

# 1.创建异步引擎
ASYNC_DATABASE_URL = 'mysql+aiomysql://root:Wordl9543@127.0.0.1:3306/fastapi_db'
#  max_overflow: 20  最大连接数  10 + 20 = 30
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True, future=True, pool_size=10,max_overflow=20)
# 2.定义模型类  基类 + 表对应的模型类
# #基类：创建时间、更新时间； 书籍表：id、书名、作者、价格、出版社

class Base(DeclarativeBase):
    crate_time:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),default=func.now,comment='创建时间')
    update_time:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),default=func.now,comment='更新时间')

class Book(Base):

    __tablename__ = 'books'
    id:Mapped[int] = mapped_column(Integer,primary_key=True,comment='书籍id')
    bookname:Mapped[str] = mapped_column(String(255),comment='书名')
    author:Mapped[str] = mapped_column(String(255),comment='作者')
    price:Mapped[float] = mapped_column(Float, comment='价格')
    publisher:Mapped[str] = mapped_column(String(255),comment='出版社')

# 3.创建表（定义函数建表---》fastapi启动时调用）
async def create_tables():
     async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




@app.on_event('startup')
async def startup_event():
    await create_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}