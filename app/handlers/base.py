from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.markdown import hbold
from loguru import logger
from app.misc import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    logger.info("User {user} start conversation with bot", user=message.from_user.id)
    await message.answer("Здравствуйте {user}!".format(
            user=hbold(message.from_user.full_name)
        )
    )


@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    try:
        raise exception
    except Exception as e:
        logger.exception("Cause exception {e} in update {update}", e=e, update=update)
    return True
