from enum import Enum

from fastapi import APIRouter, Path
from win32cryptcon import szOID_RSA_contentType

test1 = APIRouter(prefix="/test", tags=["路由传参测试"])


@test1.get("/", summary="查询所有", description="测试查询所有")
def find_all():
    print("查询所有")
    return {'message': 'OK'}


@test1.get("/{id}", summary="查询指定id用户", description="测试查询指定id用户")
def find(id: int):
    print(f"查询id为{id}的用户")
    return {'message': 'OK'}


@test1.put("/{id}", summary="更新指定id用户", description="测试更新指定id用户")
def update(id: int, name: str):
    print(f"更新id为{id}的用户为{name}")
    return {'message': 'OK'}

# 预设值传参

class EmpName(Enum):
    Momo = "莫莫"
    Jack = "杰克"
    Bob = "鲍勃"


@test1.put("/emp/{emp_name}", summary="测试预设值传参", description="预设值传参")
def update_emp(emp_name: EmpName = Path(description="员工姓名只能是枚举类中的姓名")):
    print(f"更新员工姓名为{emp_name}")
    return {'message': 'OK'}

