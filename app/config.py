from envparse import env
from app.misc import app_dir
import os
import sys

APP_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", default="")

# GOOGLE_JSON = app_dir / "promo-278508-ec16e53dedff.json"
# GSHEET_URL = 'https://docs.google.com/spreadsheets/d/1-68bZBl7C12i8skR5XRAJJyeEEx2zMtM9yoMqYzZzp8'

POSTGRES_HOST = env.str("POSTGRES_HOST", default="localhost")
POSTGRES_PORT = env.int("POSTGRES_PORT", default=5432)
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="mpasmwin32")
POSTGRES_USER = env.str("POSTGRES_USER", default="postgres")
POSTGRES_DB = env.str("POSTGRES_DB", default="promocode_bot")
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

