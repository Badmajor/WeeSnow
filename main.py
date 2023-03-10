import asyncio
import logging
from aiogram import Bot, Dispatcher, Router


from config import BOT_TOKEN, WEBHOOK_HOST, WEBHOOK_PATH
from handlers import register_routers

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)

    router = Router()

    register_routers(router)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.set_webhook(
        url=WEBHOOK_HOST + WEBHOOK_PATH,
        drop_pending_updates=True,
        allowed_updates=dp.resolve_used_update_types()
    )

if __name__ == "__main__":
    asyncio.run(main())
