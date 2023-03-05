import asyncio
import logging
from aiogram import Bot, Dispatcher, Router

from config import BOT_TOKEN
from handlers import register_default_cmds

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)

    router = Router()

    register_default_cmds(router)

    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
