from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

from youtube.app.database.requests import send_something_new

router = Router()
bot = Bot(token='6988960612:AAHzHP4MU3oLDcygDMbYjkCvXIZQGRtHyLw')

@router.message()
async def save_message(message: Message):# сохраняет новые интересные факты от пользователя
    if message.text == 'сова':
        await message.answer("Сообщение сохранено!")





