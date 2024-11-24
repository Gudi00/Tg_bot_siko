from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

from app.database.requests import send_something_new

router = Router()
bot = Bot(token='6988960612:AAHzHP4MU3oLDcygDMbYjkCvXIZQGRtHyLw')
# @router.message()
# async def save_message(message: Message):# сохраняет новые интересные факты от пользователя
#     time = message.date.now()
#     username = message.from_user.username
#     tg_id = message.from_user.id
#     fact = message.text
#     await rq.save_something_new(tg_id=tg_id, fact=fact, username=username, time=time)
#     await message.answer("Сообщение сохранено!")


# регистрация после команды start
class Registration(StatesGroup):
    user_first_name = State()
    user_last_name = State()
    extended_information = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    # await message.answer("Чтобы создать очередь, отправь сообщение в таком формате:",
    #                      reply_markup=types.ReplyKeyboardRemove()) #переписать
    # await message.answer("Иосько Михаил	3	0")
    # await message.answer("Нужно отправить весь список целиком и предерживаться шаблона: превые 2 слова должны содержать фамилию и имя, потом идёт номер текущей лабы и булевая переменная, которая отражает желание студента сдавать лабу на занятии")
    await message.answer("Введите количество студентов в группе")
    await rq.set_user(message.from_user.id)
    await state.set_state(Registration.user_first_name)


@router.message(Registration.user_first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(user_first_name=message.text)
    await state.set_state(Registration.user_last_name)  # Сместить в другую функцию
    await message.answer('Введите номер последнего, кто защищал лабу')  # переписать


@router.message(Registration.user_last_name)
async def process_last_name(message: Message, state: FSMContext):
    await state.update_data(user_last_name=message.text)
    await state.set_state(Registration.extended_information)
    await message.answer('Скидывай таблицу')


@router.message(Registration.extended_information)
async def extended_information(message: Message, state: FSMContext):
    await state.update_data(extended_information=message.text)

    data = await state.get_data()

    # const переменные
    col_columns = 4
    number_surname = 0
    number_name = 1
    number_laba = 2
    number_want = 3

    # объявление базы для расчётов
    list = []
    col_student = int(data['user_first_name'])
    was_the_last_person_to_respond = int(data['user_last_name'])

    # вввод и сохранение всех студентов

    for i in range(0, col_student):
        list.append([])
        tmp = str(data['extended_information']).split()
        list[i].append(tmp[i * col_columns + number_surname])
        list[i].append(tmp[i * col_columns + number_name])
        list[i].append(int(tmp[i * col_columns + number_laba]))
        list[i].append(int(tmp[i * col_columns + number_want]))
    print("Success! all saved")

    # выщитывание среднего количества лаб
    average_number_of_labs = 0
    for i in range(0, col_student):
        average_number_of_labs += list[i][number_laba]
    average_number_of_labs /= col_student
    print("Average number of labs: ", average_number_of_labs)

    # алгоритм для конечного вывода
    mas_rez = []
    for i in range(0, col_student):
        if list[i][number_laba] < average_number_of_labs - 2 and list[i][number_want] == 1:
            mas_rez.append(list[i])

    for i in range(0, col_student):
        number_for_check = (i + was_the_last_person_to_respond) % (col_student - 1)
        if (list[number_for_check][number_laba] >= average_number_of_labs - 2
                and list[i][number_want] == 1):
            mas_rez.append(list[number_for_check])

    for i in range(0, len(mas_rez)):
        print(f"{i+1}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")

    for i in range(0, len(mas_rez)):
        await message.answer(f"{i+1}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")
    await state.clear()
    await message.answer('Если захочешь создать новую очередь, пиши "/start"😉 ', reply_markup=kb.main)
    # await rq.update_money()

@router.message(F.text == 'Создать очередь')
async def cmd_start(message: Message, state: FSMContext):
    # await message.answer("Чтобы создать очередь, отправь сообщение в таком формате:",
    #                      reply_markup=types.ReplyKeyboardRemove()) #переписать
    # await message.answer("Иосько Михаил	3	0")
    # await message.answer("Нужно отправить весь список целиком и предерживаться шаблона: превые 2 слова должны содержать фамилию и имя, потом идёт номер текущей лабы и булевая переменная, которая отражает желание студента сдавать лабу на занятии")
    await message.answer("Введите количество студентов в группе")
    await rq.set_user(message.from_user.id)
    await state.set_state(Registration.user_first_name)


@router.message(Registration.user_first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(user_first_name=message.text)
    await state.set_state(Registration.user_last_name)  # Сместить в другую функцию
    await message.answer('Введите номер последнего, кто защищал лабу')  # переписать


@router.message(Registration.user_last_name)
async def process_last_name(message: Message, state: FSMContext):
    await state.update_data(user_last_name=message.text)
    await state.set_state(Registration.extended_information)
    await message.answer('Скидывай таблицу')


@router.message(Registration.extended_information)
async def extended_information(message: Message, state: FSMContext):
    await state.update_data(extended_information=message.text)

    data = await state.get_data()

    # const переменные
    col_columns = 4
    number_surname = 0
    number_name = 1
    number_laba = 2
    number_want = 3

    # объявление базы для расчётов
    list = []
    col_student = int(data['user_first_name'])
    was_the_last_person_to_respond = int(data['user_last_name'])

    # вввод и сохранение всех студентов

    for i in range(0, col_student):
        list.append([])
        tmp = str(data['extended_information']).split()
        list[i].append(tmp[i * col_columns + number_surname])
        list[i].append(tmp[i * col_columns + number_name])
        list[i].append(int(tmp[i * col_columns + number_laba]))
        list[i].append(int(tmp[i * col_columns + number_want]))
    print("Success! all saved")

    # выщитывание среднего количества лаб
    average_number_of_labs = 0
    for i in range(0, col_student):
        average_number_of_labs += list[i][number_laba]
    average_number_of_labs /= col_student
    print("Average number of labs: ", average_number_of_labs)

    # алгоритм для конечного вывода
    mas_rez = []
    for i in range(0, col_student):
        if list[i][number_laba] < average_number_of_labs - 2 and list[i][number_want] == 1:
            mas_rez.append(list[i])

    for i in range(0, col_student):
        number_for_check = (i + was_the_last_person_to_respond) % (col_student - 1)
        if (list[number_for_check][number_laba] >= average_number_of_labs - 2
                and list[i][number_want] == 1):
            mas_rez.append(list[number_for_check])

    for i in range(0, len(mas_rez)):
        print(f"{i+1}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")

    for i in range(0, len(mas_rez)):
        await message.answer(f"{i+1}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")
    await state.clear()
    await message.answer('Если захочешь создать новую очередь, пиши "/start"😉 ', reply_markup=kb.main)

# Конец регистрации пользователя

# # регистрация после команды start
# class Registration(StatesGroup):
#     user_first_name = State()
#     user_last_name = State()
#     extended_information = State()
#     phone_number = State()
#
#
# @router.message(CommandStart())
# async def cmd_start(message: Message, state: FSMContext):
#     await message.answer("Привет🙃 Я cмогу тебе рассказать множество забавных фактов или предоставить возможность написать анонимное сообщение создателю",
#                          reply_markup=types.ReplyKeyboardRemove()) #переписать
#     await message.answer("Но для начала давай познакомимся😊")
#     await message.answer("Как тебя зовут?")
#     await rq.set_user(message.from_user.id)
#     await state.set_state(Registration.user_first_name)
#
#
# @router.message(Registration.user_first_name)
# async def process_first_name(message: Message, state: FSMContext):
#     await state.update_data(user_first_name=message.text)
#     await state.set_state(Registration.user_last_name)#Сместить в другую функцию
#     await message.answer('А какая у тебя фамилия?') #переписать
#     await message.answer("😅")
#
#
# @router.message(Registration.user_last_name)
# async def process_last_name(message: Message, state: FSMContext):
#     await state.update_data(user_last_name=message.text)
#     await state.set_state(Registration.extended_information)
#     await message.answer('Расскажи что-нибудь о себе')
#
#
# @router.message(Registration.extended_information)
# async def extended_information(message: Message, state: FSMContext):
#     await state.update_data(extended_information=message.text)
#     await state.set_state(Registration.phone_number)
#     await message.answer('И последнее: отправьте свой номер телефона', reply_markup=kb.get_number)
#
#
# @router.message(Registration.phone_number, F.contact)
# async def register_number(message: Message, state: FSMContext):
#     await state.update_data(phone_number=message.contact.phone_number)
#     data = await state.get_data()
#
#     contact = message.contact
#     tg_id = contact.user_id
#     phone_number = contact.phone_number
#     tg_user_first_name = contact.first_name
#     tg_user_last_name = contact.last_name
#     time = message.date.now()
#     username = message.from_user.username
#     await rq.save_user(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
#                        user_first_name=data['user_first_name'], tg_user_last_name=tg_user_last_name,
#                        user_last_name=data['user_last_name'], phone_number=phone_number,
#                        extended_information=data['extended_information'], time=time,
#                        username=username)
#     await message.answer(f'Приятно познакомится, {data['user_first_name']}, {data['user_last_name']}', reply_markup=kb.main)
#     await state.clear()
#     await message.answer('Если захочешь изменить введённые данные, то можешь написать "/start"😉')
#     # await rq.update_money()
# # Конец регистрации пользователя





#Интересные факты и глубже
@router.message(F.text == 'Интересные факты')
async def catalog(message: Message):
    await message.answer('В этой категории можно узнать более 200 интересных и забавных фактов🤘)', reply_markup=kb.interesting_facts)


@router.message(F.text == 'Что-то новое')
async def catalog(message: Message):
    fact = await send_something_new()
    if fact:
        await message.answer('Лови новый факт🙂', reply_markup = types.ReplyKeyboardRemove())
        await message.answer(fact, reply_markup=kb.more_something_new)
    else:
        await message.answer("Извините, что-то пошло не так.", reply_markup=kb.interesting_facts)

@router.callback_query(F.data == 'something_new')
async def catalog(callback: CallbackQuery):
    fact = await send_something_new()
    if fact:
        await callback.answer('')
        await callback.message.answer(fact, reply_markup=kb.more_something_new)
    else:
        await callback.answer('')
        await callback.message.answer("Извините, что-то пошло не так.", reply_markup=kb.interesting_facts)

@router.callback_query(F.data == 'back_to_interesting_facts')
async def to_main(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы вернулись назад😶‍🌫️', reply_markup=kb.main)








class for_me(StatesGroup):
    user_message = State()

@router.message(F.text == 'Рекомендации для разработчика')
async def start_saving_for_creator(message: Message, state: FSMContext):
    await message.answer("Теперь ты можешь отпавить сообщение для разработчика", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(for_me.user_message)

@router.message(for_me.user_message)
async def saving_for_creator(message: Message, state: FSMContext):
    await state.update_data(user_message=message.text)
    data = await state.get_data()
    tg_id = message.from_user.id
    tg_user_first_name = message.from_user.first_name
    tg_user_last_name = message.from_user.last_name
    time = message.date.now()
    username = message.from_user.username
    await rq.save_user_message(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                        tg_user_last_name=tg_user_last_name, user_message=data['user_message'],
                        time=time, username=username)
    await state.clear()
    await message.answer('Ваше сообщение сохранено', reply_markup=kb.main)











# anonymous message
class anonymous_for_me(StatesGroup):
    anonymous_user_message = State()

@router.message(F.text == 'Анонимное сообщение Мише')
async def start_anonymous_saving_for_creator(message: Message, state: FSMContext):
    await message.answer("Теперь ты можешь отпавить аноимное сообщение Мише", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(anonymous_for_me.anonymous_user_message)

@router.message(anonymous_for_me.anonymous_user_message)
async def anonymous_saving_for_creator(message: Message, state: FSMContext):
    await state.update_data(anonymous_user_message=message.text)
    data = await state.get_data()
    tg_id = message.from_user.id
    tg_user_first_name = message.from_user.first_name
    tg_user_last_name = message.from_user.last_name
    time = message.date.now()
    username = message.from_user.username
    await rq.anonymous_save_user_message(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                        tg_user_last_name=tg_user_last_name, anonymous_user_message=data['anonymous_user_message'],
                        time=time, username=username)
    await state.clear()
    await message.answer('Ваше анонимное сообщение сохранено', reply_markup=kb.main)


@router.message(F.text == 'На главную')
async def to_main(callback: CallbackQuery):
    await callback.answer('Выберите категорию ^_^', reply_markup=kb.main)

# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('Вы нажали на кнопку помощи) Что у вас произошло?')


# @router.message(F.text == 'Каталог')
# async def catalog(message: Message):
#     await message.answer('Выберите категорию товара',
#     reply_markup=await kb.categories())
#
#
# @router.callback_query(F.data.startswith('category_'))
# async def category(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию')
#     await callback.message.answer('Выберите товар по категории',
#                                   reply_markup=await kb.items(callback.data.split('_')[1]))
#
#
# @router.callback_query(F.data.startswith('item_'))
# async def category(callback: CallbackQuery):
#     item_data = await rq.get_item(callback.data.split('_')[1])
#     await callback.answer('Вы выбрали товар')
#     await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')
