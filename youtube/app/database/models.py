from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Something_new(Base):
    __tablename__ = "something_new"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    fact: Mapped[str] = mapped_column(String(400), nullable=True, default=None)
    username: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)

class Person(Base):
    __tablename__ = 'person'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_last_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    user_last_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    phone_number: Mapped[int] = mapped_column(nullable=True, default=None)
    extended_information: Mapped[str] = mapped_column(String(320), nullable=True, default=None)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)
    ban_information: Mapped[int] = mapped_column(default=1)

class Pixel(Base):
    __tablename__ = 'pixels'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    money: Mapped[int] = mapped_column(default=0)


class User_message(Base):
    __tablename__ = 'user_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_last_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    user_message: Mapped[str] = mapped_column(String(520), nullable=True, default=None)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)

class Anonymous_user_message(Base):
    __tablename__ = 'anonymous_user_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_last_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    anonymous_user_message: Mapped[str] = mapped_column(String(520), nullable=True, default=None)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)
# class option_1(Base):
#     __tablename__ = 'all_option_1'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(25))
#     progress: Mapped[int] = mapped_column(default=0)
#
#
# class Categore_for_option_2(Base):
#     __tablename__ = 'categories_for_option_2'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(25))
#     description: Mapped[str] = mapped_column(String(120))
#     price: Mapped[int] = mapped_column(default=0)
#     category: Mapped[int] = mapped_column(ForeignKey('option_1.id'))


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
