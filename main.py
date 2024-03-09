import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from app.handlers import router

from app.configure import TOKEN
dp = Dispatcher()



async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except:
        print("Tugadi)")