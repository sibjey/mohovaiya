from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=False)
