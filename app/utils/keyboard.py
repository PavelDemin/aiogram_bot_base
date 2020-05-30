from typing import Tuple, Union
from aiogram.utils.callback_data import CallbackData
from app.misc import bot, dp, i18n
from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)


cb_change = CallbackData("change", "property", "value")


_ = i18n.lazy_gettext

CONFIRM = [
    _("Yes"),
    _("No"),
]


def choose_language_markup() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    for code, language in i18n.AVAILABLE_LANGUAGES.items():
        markup.add(
            types.InlineKeyboardButton(
                language.label, callback_data=cb_change.new(property="language", value=code)
            )
        )
    return markup


def confirm_markup(button: list, value = None) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=button[0],
                callback_data=cb_change.new(
                    property="confirm",
                    value=value
                )
            ),
            InlineKeyboardButton(
                text=button[1],
                callback_data=cb_change.new(
                    property="cancel",
                    value=value
                )
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


# def main_menu_markup():
#     return ReplyKeyboardMarkup(resize_keyboard=True, selective=True, keyboard=[
#         [
#             KeyboardButton(text=MAIN_MENU[0]),
#             KeyboardButton(text=MAIN_MENU[1]),
#             KeyboardButton(text=MAIN_MENU[2]),
#         ],
#         [
#             KeyboardButton(text=MAIN_MENU[3]),
#             KeyboardButton(text=MAIN_MENU[4]),
#             KeyboardButton(text=MAIN_MENU[5])
#         ],
#         [
#             KeyboardButton(text=MAIN_MENU[6])
#         ]
#     ])
#
#
# def sub_menu_markup() -> InlineKeyboardMarkup:
#     inline_keyboard = [
#         [InlineKeyboardButton(
#             text=SUB_MENU[i],
#             callback_data=cb_settings.new(
#                 property="sub_menu_" + str(i),
#                 value="1"
#             )
#         )] for i in range(len(SUB_MENU))]
#     return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

