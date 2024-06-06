from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config import BOT_TOKEN
from bot.handlers.user_handlers import router
from bot.keyboards.menu_left import set_bot_commands


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    await set_bot_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
