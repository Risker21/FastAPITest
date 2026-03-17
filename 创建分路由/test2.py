from fastapi import APIRouter, Query

test2 = APIRouter(prefix="/test2", tags=["URL路由传参测试"])

@test2.get("/findall", summary="查询所有", description="测试URL传参")
def find_all(id: int = Query(default=None, description="员工id"),
             name: str = Query(default=None, description="员工姓名"),
             age: int = Query(default=None, description="员工年龄")):
    print(id, name, age)
    return {"msg": "OK"}


# 数据校验
@test2.get("/addemp", summary="添加数据测试", description="检验数据")
def add_emp(name:str = Query(default=None, description="员工姓名",min_length=2,max_length=9),
             age: int = Query(default=None, description="员工年龄",gt=20,lt=100)):
    print(f"添加{name},年龄{age}")
    return {"msg": "OK"}

