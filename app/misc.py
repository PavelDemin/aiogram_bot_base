from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from app import config


bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    from app.utils import executor
    logger.info("Configure handlers...")
    # noinspection PyUnresolvedReferences
    import app.handlers
    executor.setup()




