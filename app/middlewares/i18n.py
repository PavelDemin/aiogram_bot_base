from dataclasses import dataclass, field
from typing import Any, Tuple
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware


@dataclass
class LanguageData:
    flag: str
    title: str
    label: str = field(init=False, default=None)

    def __post_init__(self):
        self.label = f"{self.flag} {self.title}"


class I18nMiddleware(BaseI18nMiddleware):
    AVAILABLE_LANGUAGES = {
        "en": LanguageData("🇺🇸", "English"),
        "ru": LanguageData("🇷🇺", "Русский"),
        # "uk": LanguageData("🇺🇦", "Українська"),
    }

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        tg_user = types.User.get_current()
        *_, data = args
        # user = await get_user(tg_user.id)
        user = None
        if user is None or tg_user is None:
            data['locale'] = 'en'
            return 'en'
        else:
            data['locale'] = user.language
            data['user'] = user.user_name
            lang = user.language
            return lang
