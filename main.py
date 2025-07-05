import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "7736149860:AAEd9QqxIuO53k2KZEOqt2c7YIwP5PmB730"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Здарова, Ржавый! Чё по тачкам ищем?")

@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты сказал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
