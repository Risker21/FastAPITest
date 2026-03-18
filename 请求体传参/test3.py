from datetime import date
from enum import Enum

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field, field_validator
from pygments.lexer import default

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
    name: str = Field(description="姓名")
    age: int = Field(description="年龄",default=18,lt=65,ge=18)
    gender: Gender = Field(description="性别")
    birthday: date = Field(description="出生日期")
    address: Addr = Field(description="地址")

    @field_validator('name')
    def validate_name(cls,value):
        pass
        import re
        result = re.match(r'^[a-zA-Z_]\w{2,7}$',value)
        assert result is not None
        return value

@test3.post("/add", summary="添加员工", description="添加员工信息")
def find_all(emp: Emp):
    print(emp)
    return {"msg": "OK"}

'''
请求体传参
'''
@test3.post("/test3/select", summary="请求体传参", description="测试请求体传参")
def test(name:str = Body(default = None,summary="姓名",description="姓名描述"),
         age:int = Body(default = 18,lt=65,ge=18)):
    print(f'姓名：{name}，年龄：{age}')
    return {"msg": "OK"}




