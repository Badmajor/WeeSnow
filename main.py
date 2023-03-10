import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

from config import BOT_TOKEN, WEBHOOK_HOST, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
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
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=WEBAPP_HOST, port=WEBAPP_PORT)
    await site.start()

    # Running it forever
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
