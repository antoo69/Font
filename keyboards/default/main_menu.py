
from aiogram import types

menu_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(
                text="📋 Daftar Font 📝"
            ),
            types.KeyboardButton(
                text="☑️ Setujui Semua font ✅"
            ),
        ],
        [
            types.KeyboardButton(
                text="🤖 About Inline Mode 📃"
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
