import asyncio
import logging
import random

from aiogram import Bot, Dispatcher,F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import TOKEN
from config import photo1
from config import photo2


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer("Привет вы запустили игру, Введите число от 1 до 3  ")

@dp.message()
async def start_random(message: Message):
        user = int(message.text)
        number = random.choice([1, 2, 3])
        if user == number:
            await message.answer_photo(photo1)
        else:
            await message.answer_photo(photo2)
        print(f"Загадонное число было {number}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
 

