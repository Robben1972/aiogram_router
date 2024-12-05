from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def generate_reply_keyboard() -> ReplyKeyboardMarkup: 
    kb = ReplyKeyboardBuilder()
    kb.button(text='Yes')
    kb.button(text='No')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)