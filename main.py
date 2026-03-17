from fastapi import FastAPI

from 创建分路由.test import test
from 创建分路由.test2 import test2
from 请求体传参.test3 import test3
from 路由传参.test1 import test1

app = FastAPI()

app.include_router(test)
app.include_router(test1)
app.include_router(test2)
app.include_router(test3)




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
