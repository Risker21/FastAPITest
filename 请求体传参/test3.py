from datetime import date
from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel, Field

test3 = APIRouter(prefix="/test3", tags=["请求体传参测试"])


class Addr(BaseModel):
    province: str = Field(description="省份")
    city: str = Field(description="城市")
    district: str = Field(description="区县")

    def __str__(self):
        return f"{self.province}{self.city}{self.district}"


class Gender(Enum):
    MALE = "男"
    FEMALE = "女"
    OTHER = "未知"



class Emp(BaseModel):
    name: str
    age: int
    gender: Gender
    birthday: date
    address: Addr

@test3.post("/add", summary="添加员工", description="添加员工信息")
def find_all(emp: Emp):
    print(emp)
    return {"msg": "OK"}
