

from config import labeler, api, user

from vkbottle import User, GroupEventType, GroupTypes
from loguru import logger
from vkbottle import ErrorHandler
import asyncio
import sys





from main_module import *





labeler.load(main_labeler) # Основной модуль ✅
labeler.load(test_labeler) # Тестовый модуль
labeler.load(profile_labeler)
labeler.load(math_labeler)



labeler.load(rp_labeler) # Рп модуль  ОСТАВЛЯТЬ ПОСЛЕДНИМ✅
labeler.load(pres_bet_labeler) # Пресбет модуль ОСТАВЛЯТЬ ПОСЛЕДНИМ✅

logger.disable("vkbottle")

# Автоматическая ротация по объему файла
logger.add("Logging_1.log", rotation="500 MB")
# Новый файл создается каждый день в 12:00
# logger.add("Logging_1.log", rotation="12:00")
# Автоматическая ротация 1 раз в неделю
# logger.add("Logging_1.log", rotation="1 week")
# Удаляет лог-файлы старше 10 days
# logger.add("Logging_1.log", retention="10 days")
# Сжимает лог-файл
# logger.add("Logging_1.log", compression="zip")


logger.debug('________________\n')
logger.debug(' СТАРТ ГРИМА')
logger.debug('________________')



user= User(api=api,
labeler=labeler)


user.run_forever()