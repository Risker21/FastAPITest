from fastapi import APIRouter

emp = APIRouter(prefix="/emp", tags=["企业员工"])

@emp.get("emp/{id}")
def get_emp(id:int):
    print(f'根据{id}查询企业员工')
    return {'message': 'OK'}
