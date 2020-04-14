from aiogram.utils.executor import Executor
from app.misc import dp
from app.models import db
from aiogram import Dispatcher
from loguru import logger


runner = Executor(dp)


def setup():
    logger.info("Configure executor...")
    db.setup(runner)
    runner.start_polling(dp)
