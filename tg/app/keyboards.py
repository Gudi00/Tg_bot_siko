from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

more_something_new = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ещё фактов!', callback_data='something_new'),
    InlineKeyboardButton(text='Назад', callback_data='back_to_interesting_facts')]])

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Интересные факты')],
     #                                [KeyboardButton(text='Темы на подумать')],
                                     [KeyboardButton(text='Анонимное сообщение Мише')],
                                      [KeyboardButton(text='Рекомендации для разработчика')]], #сайт знакомств
                           resize_keyboard=True,
                           input_field_placeholder="Дорогой друг, выбери категорию(●'◡'●)")


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

interesting_facts = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Что-то новое'),
 #   KeyboardButton(text='О создателе')],
 #   [KeyboardButton(text='Написать своё'),
    KeyboardButton(text='На главную')]],
resize_keyboard=True)

# interesting_facts = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Что-то новое', callback_data='something_new')],
#     [InlineKeyboardButton(text='О создателе', callback_data='about_me')],
#     [InlineKeyboardButton(text='Написать своё', callback_data='message_from_friends')],
#     [InlineKeyboardButton(text='На главную', callback_data='to_main')]])


# async def categories():
#     all_categories = await get_categories()
#     keyboard = InlineKeyboardBuilder()
#     for category in all_categories:
#         keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()
#
#
# async def items(category_id):
#     all_items = await get_category_item(category_id)
#     keyboard = InlineKeyboardBuilder()
#     for item in all_items:
#         keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()
