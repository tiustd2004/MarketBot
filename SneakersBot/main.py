
from aiogram import Bot, Dispatcher, types
from aiogram import F

from aiogram.types import URLInputFile
from aiogram.filters import Command
import asyncio
from config import TOKEN_API,ADMIN_CHAT_ID
bot = Bot(TOKEN_API)
dp = Dispatcher()


kb_1 = [
    [types.KeyboardButton(text="Активная пена очиститель - 280 руб")],
    [types.KeyboardButton(text="Дезодорант для обуви - 338 руб")],
    [types.KeyboardButton(text="Белая краска для обуви - 207 руб")],
    [types.KeyboardButton(text='Назад🔙')]
]

kb_0 = [  
        [types.KeyboardButton(text = 'Назад🔙')] 
        ]

kb_2 = [
    [types.KeyboardButton(text="🔨Ремонт🔨")],
    [types.KeyboardButton(text="🧹Клининг🧹")],
    [types.KeyboardButton(text="🦠Купить очищающие средства для обуви🦠")]
]

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Привет😺! Я информационный бот🤖, который поможет тебе ознакомиться с вайбом нашей компании🌟')

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_2,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )

    await message.answer("⚡Твоё меню⚡", reply_markup=keyboard)

@dp.message(F.text.contains('🔨Ремонт🔨'))
async def cmd_first_s(message: types.Message):
    await message.answer('Пришли фото обуви сюда и наш мастер сам оценит состояние и напишет цену в ЛС')
    await message.answer('🚨Сделайте конфеденциальность до минимума, чтобы наш мастер смог связаться с вами🚨')
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_0,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )
    await message.answer('Ты можешь вернуться обратно',reply_markup=keyboard)


@dp.message(F.text.contains('🧹Клининг🧹'))
async def cmd_second_s(message: types.Message):
    await message.answer('Пришли фото обуви сюда и наш мастер сам оценит состояние и напишет цену в ЛС')
    await message.answer('🚨Сделайте конфеденциальность до минимума, чтобы наш мастер смог связаться с вами🚨')
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_0,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )
    await message.answer('Ты можешь вернуться обратно',reply_markup=keyboard)


@dp.message(F.text.contains('🦠Купить очищающие средства для обуви🦠'))
async def market (message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_1,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )

    await message.answer("⚡Твоё меню⚡", reply_markup=keyboard)
    
    

@dp.message(F.text.contains('Активная пена очиститель - 280 руб'))
async def first_market (message: types.Message):
    await message.answer('Номер для перевода: 89320997945')
    await message.answer('Пришлите скриншот оплаты, чтобы наш мастер проверил сумму и написал вам когда можно забрать товар' + '\n' + 'В сообщении желательно сразу писать какой товар вы заказали')


@dp.message(F.text.contains('Дезодорант для обуви - 338 руб'))
async def first_market (message: types.Message):
    await message.answer('Номер для перевода: 89320997945')
    await message.answer('Пришлите скриншот оплаты, чтобы наш мастер проверил сумму и написал вам когда можно забрать товар' + '\n' + 'В сообщении желательно сразу писать какой товар вы заказали')


@dp.message(F.text.contains('Белая краска для обуви - 207 руб'))
async def first_market (message: types.Message):
    await message.answer('Номер для перевода: 89320997945')
    await message.answer('Пришлите скриншот оплаты, чтобы наш мастер проверил сумму и написал вам когда можно забрать товар' + '\n' + 'В сообщении желательно сразу писать какой товар вы заказали')

@dp.message(F.text.contains('Назад🔙'))
async def back_menu (message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_2,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )

    await message.answer("⚡Твоё меню⚡", reply_markup=keyboard)

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    user_info = f"{message.from_user.first_name} {message.from_user.last_name} (@{message.from_user.username})"
    await bot.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo.file_id, caption=user_info)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())