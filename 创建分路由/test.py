
from fastapi import APIRouter

test = APIRouter(prefix='/test', tags=["分路由测试"])

@test.get("/find", summary="查询操作", description="测试查询操作")
def find():
    print("查询操作")
    return {'message': 'OK'}

@test.post("/add", summary="添加操作", description="测试添加操作")
def add():
    print("添加操作")
    return {'message': 'OK'}
