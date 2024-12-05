from aiogram import Router, F
from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.filters import Command

from keyboards.for_questions import generate_reply_keyboard


router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Do you love your job?', reply_markup=generate_reply_keyboard())


@router.message(F.text.lower() == "yes")
async def answer_yes(message: Message):
    await message.answer(
        "That is good!",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower() == "no")
async def answer_no(message: Message):
    await message.answer(
        "Really :( ...",
        reply_markup=ReplyKeyboardRemove()
    )
