from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import DateTime, func, Integer, create_engine, String, Enum, JSON
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine("mysql+pymysql://root:Wordl9543@127.0.0.1:3306/fastapi_db", echo=True, future=True, pool_size=10,
                       max_overflow=20)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Gender(Enum):
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
    gender: Mapped[Gender] = mapped_column(Gender, default=Gender.unknown, comment='性别')
    # 使用 JSON 类型存储地址信息
    address: Mapped[dict] = mapped_column(JSON, comment='用户地址')


if __name__ == '__main__':
    # 创建所有表
    Base.metadata.create_all(engine)

    # 创建会话并添加数据
    db = SessionLocal()
    try:
        # 创建一个用户
        user = User(
            username="testuser",
            gender=Gender.male,
            address={"province": "北京市", "city": "北京市"}
        )
        db.add(user)
        db.commit()
        print("用户创建成功")
    finally:
        db.close()
