import enum
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import DateTime, func, Integer, create_engine, String, JSON, Enum
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine("mysql+pymysql://root:Wordl9543@127.0.0.1:3306/fastapi_db", echo=True, future=True, pool_size=10,
                       max_overflow=20)


class Gender(enum.Enum):
    male = '男'
    female = '女'
    unknown = '未知'


class Addr(BaseModel):
    province: str
    city: str


# 3.定义模型类  基类 + 表对应的模型类
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), comment='创建时间')
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), onupdate=func.now(),
                                                  comment='更新时间')


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='用户id')
    username: Mapped[str] = mapped_column(String(255), unique=True, comment='用户名')
    gender: Mapped[Gender] = mapped_column(Enum(Gender, values_callable=lambda x: [e.value for e in x]),
                                           default=Gender.unknown, comment='性别')
    # 使用 JSON 类型存储地址信息
    address: Mapped[dict] = mapped_column(JSON, comment='用户地址')


if __name__ == '__main__':
    # 创建所有表
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    with session.begin():
        emp1 = User(id=1, username='Momo', gender=Gender.male, address={'province': '北京市', 'city': '东城区'})
        emp2 = User(id=2, username='Lily', gender=Gender.female, address={'province': '重庆市', 'city': '江北区'})
        emp3 = User(id=3, username='Eva', gender=Gender.unknown, address={'province': '广东省', 'city': '广州市'})
        emp4 = User(id=4, username='Tom', gender=Gender.male, address={'province': '重庆市', 'city': '沙坪坝区'})

        session.add_all([emp1, emp2, emp3, emp4])
