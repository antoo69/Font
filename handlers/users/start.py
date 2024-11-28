from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default.main_menu import menu_button
from utils.db_api.bot_users import create_bot_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    txt1 = f"<i>Halo</i> <b>{message.from_user.full_name},</b>"
    txt1 += "\nWelcome to ꜰ໑ʀᴆɪ Changer bot"
    txt1 += "\n\nDengan bot ini, anda bisa mengubah text anda menjadi font yang berbeda."
    await message.answer(text=txt1)
    txt2 = "<i>Silahkan pilih font </i> <b>📋 Daftar Font 📝 </b> <i>section, \
        \nor click</i> <b>☑️ Setujui Semua Font ✅</b><i> tombol untuk menggunakan semua font sekaligus</i>"
    await message.answer(text=txt2, reply_markup=menu_button)

    # User'ni database'ga saqlaymiz
    create_bot_user(message.from_user)
