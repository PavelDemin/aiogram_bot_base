from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.middlewares.i18n import I18nMiddleware
from loguru import logger
from app import config


app_dir: Path = Path(__file__).parent.parent
locales_dir = app_dir / "locales"
bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
i18n = I18nMiddleware("bot", locales_dir, default="ru")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    from app.utils import executor
    from app import middlewares
    middlewares.setup(dp)
    logger.info("Configure handlers...")
    # noinspection PyUnresolvedReferences
    import app.handlers
    executor.setup()




