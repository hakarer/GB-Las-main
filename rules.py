from vkbottle.user import Message
# from config import db
import asyncio
import datetime
from async_lru import alru_cache
from vkbottle.dispatch.rules import ABCRule
from config import prefixes
from vkbottle.tools.dev.mini_types.base import BaseMessageMin



class From_Me(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        from main_module.main_function import Main_user
        return (event.from_id == Main_user.id)

class Prefix(ABCRule):
    async def check(self, message: Message) -> bool:
        # Проверяем, начинается ли текст сообщения с одного из префиксов
        return any(message.text.startswith(prefix) for prefix in prefixes)

    async def get_text_msg(self, message: Message) -> str:
        # Удаляем префикс из текста сообщения
        for prefix in prefixes:
            if message.text.startswith(prefix):
                return message.text[len(prefix):].strip()
        return message.text  # Если префикс не найден, возвращаем оригинальный текст
    
    async def get_text(self, text: str) -> str:
        # Удаляем префикс из текста сообщения
        for prefix in prefixes:
            if text.startswith(prefix):
                return text[len(prefix):].strip()
        return text  # Если префикс не найден, возвращаем оригинальный текст
    

