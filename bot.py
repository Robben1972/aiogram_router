import asyncio
from aiogram import Dispatcher, Bot
from environs import Env
from handlers import different_questions, questions

env = Env()
env.read_env()

async def main():
    bot = Bot(token=env('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(questions.router, different_questions.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())