import random

from app.database.models import async_session
from app.database.models import Category, Item, Person, User

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from app.database.models import Something_new, User_message, Anonymous_user_message, Pixel


async def send_something_new():
    async with async_session() as session:
        return await session.scalar(select(Something_new.fact).where(Something_new.id == random.randint(1,254)))




async def save_something_new(tg_id, fact, username, time):
    async with async_session() as session:
        session.add(Something_new(tg_id=tg_id, fact=fact, username=username, time=time))
        await session.commit()


async def update_money(tg_id, amount):
    async with async_session() as session:
        stmt = update(Pixel).where(Pixel.id == 1).values(name='Новое значение')
        session.execute(stmt)
        session.commit()
async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def save_user(tg_id, tg_user_first_name,
                    user_first_name, tg_user_last_name,
                    user_last_name, phone_number,
                    extended_information, time, username):
    async with async_session() as session:
        session.add(Person(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                       user_first_name=user_first_name, tg_user_last_name=tg_user_last_name,
                       user_last_name=user_last_name,
                       extended_information=extended_information, time=time, username=username))
        await session.commit()

# async def save_user(tg_id, tg_user_first_name,
#                     user_first_name, tg_user_last_name,
#                     user_last_name, phone_number,
#                     extended_information, time, username):
#     async with async_session() as session:
#         session.add(Person(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
#                        user_first_name=user_first_name, tg_user_last_name=tg_user_last_name,
#                        user_last_name=user_last_name, phone_number=phone_number,
#                        extended_information=extended_information, time=time, username=username))
#         await session.commit()

async def save_user_message(tg_id, tg_user_first_name,
                        tg_user_last_name, user_message,
                        time, username):
    async with async_session() as session:
        session.add(User_message(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                            tg_user_last_name=tg_user_last_name, user_message=user_message,
                            time=time, username=username))
        await session.commit()

async def anonymous_save_user_message(tg_id, tg_user_first_name,
                        tg_user_last_name, anonymous_user_message,
                        time, username):
    async with async_session() as session:
        session.add(Anonymous_user_message(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                            tg_user_last_name=tg_user_last_name, anonymous_user_message=anonymous_user_message,
                            time=time, username=username))
        await session.commit()

#
# async def get_option():
#     async with async_session() as session:
#         return await session.scalars(select(option_1))
async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

# async def get_categories_for_option(category_id):
#     async with async_session() as session:
#         return await session.scalars(select(Categore_for_option_2).where(Categore_for_option_2.category == category_id))
async def get_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))


# async def get_item(item_id):
#     async with async_session() as session:
#         return await session.scalar(select(Item).where(Item.id == item_id))
async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
