from asyncio import sleep
from vkbottle import (
    API, Callback, GroupEventType, GroupTypes, KeyboardButtonColor,
    Text, OpenLink, Keyboard, ShowSnackbarEvent, VKAPIError, ErrorHandler,
) 
from vkbottle.user import User, Message, Blueprint
from vkbottle.dispatch.rules.base import (
    CommandRule, ChatActionRule, FromPeerRule, RegexRule,
)
from loguru import logger
from sympy import symbols, Eq, solve, sympify
from vkbottle import CaptchaError
import re
from transliterate import translit
import asyncio
import vkbottle
from transliterate import translit
from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import vk_api
import json
import io
from vkbottle.dispatch.rules.base import CommandRule
from vk_api.vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.exceptions import VkApiError
from io import BytesIO
import labeler
import time
from vkbottle.bot import BotLabeler
from vkbottle import Bot
from datetime import timedelta
import base64
from googletrans import Translator
import random, requests
from vkbottle.bot import Blueprint, Message
from vk_api.upload import VkUpload
from typing import Optional
import requests
from bs4 import BeautifulSoup
from vk_api.utils import get_random_id
import pyperclip
from typing import List

import webbrowser
import asyncio
import aiohttp
import orjson

from    os    import  system
from   time   import   time   as unixtime
from datetime import datetime

from pick import  pick
from pick import Option

from vkbottle import API
from vkbottle import User
from vkbottle.user import Message

from vkbottle_types.responses.users    import UsersUserFull
from vkbottle_types.responses.messages import MessagesMessage

from loguru import logger 



import aiohttp
import asyncio
import ssl
import certifi
import ssl

# Disabling SSL verification (not recommended for production)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE





#Отключение логов вк
from loguru import logger
logger.disable("vkbottle")
bp = Blueprint()
users = []
translator = Translator()
YOUR_USER_ID = 272730292


bl = BotLabeler()
connected_users = {}
TOKEN = API
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
# Создайте Blueprint для команды
add_user_bp = Blueprint()

# Создайте словарь для хранения API токенов пользователей
user_tokens = {}
YOUR_API_TOKEN = API
#подключение к апи
api = API(token='vk1.a.w6kQa_xr6GcXMIDft5_4AWva2cK_rXeESQJvFrt_zagHCRHOGU_55UOJ86ci9Yrre1Wbe6PC_-Ne32L7xdPYnOmmtSWZl1W8DqlPlBWWla_2hKoEqUL-IOPNE--uQ6P512ny6-E3ywj8ZXj_1QEZ-pOBCFBK2rbM6J-R_mcyFgqJ8t27PxoyXcnU4HSNA635Vuygv4FqnqKX8C_ev_JgYg')
bp = User()

#создание юзера
user = User(api=api)
#реагирование на разный регистр текста
user.labeler.vbml_ignore_case = True
#константа айди
MAIN_ID= 272730292



TEMPLATE_FILE = "templates.json"


#Автокапча, отключил пока что, потом сделаем
# async def captcha_handler(e: CaptchaError) -> str:
#     code, accuracy = solver.solve(url=e.img, minimum_accuracy=0.40, repeat_count=14)
#     await sleep(5)
#     logger.warning(f"решение капчи \ncaptcha: {e.img}\t| solving: {code} \t| accuracy: {accuracy}")
#     return code






# Функция для получения строкового представления пола
def get_gender_string(sex):
    if sex == 1:
        return 'Женский'
    elif sex == 2:
        return 'Мужской'
    else:
        return 'Не указан'

def format_account_age(delta):
    years, months, days = delta.years, delta.months, delta.days
    hours = delta.hours

    if days == 1:
        days_text = "1 день"
    elif days % 10 in {2, 3, 4} and days not in {12, 13, 14}:
        days_text = f"{days} дня"
    else:
        days_text = f"{days} дней"

    if hours == 1:
        hours_text = "1 час"
    elif hours % 10 in {2, 3, 4} and hours not in {12, 13, 14}:
        hours_text = f"{hours} часа"
    else:
        hours_text = f"{hours} часов"

    years_text = f"{years} {'год' if years == 1 else 'года' if 2 <= years <= 4 else 'лет'}"
    months_text = f"{months} {'месяц' if months == 1 else 'месяца' if 2 <= months <= 4 else 'месяцев'}"

    age_text = f"{years_text} {months_text} {days_text}."

    return age_text

def format_timedelta(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        return f"{days} дней {hours} часов {minutes} минут"
    elif hours > 0:
        return f"{hours} часов {minutes} минут"
    elif minutes > 0:
        return f"{minutes} минут"
    else:
        return f"{seconds} секунд"

    # Обработчик команды "gb проверь айди"






@user.on.message(text=["gb инфо", "гб инфо", "<ваш_префикс> инфо"])
async def remove_trusted_33user(message: Message):
   command_prefixes = ["gb", "гб", "<ваш_префикс>"]
   if message.from_id == MAIN_ID:
 # Получаем префикс пользователя из файла
       prefixes = load_prefixes()
       user_prefixes = prefixes.get(str(message.from_id), ["gb"])  # Если префикс не установлен, используем "gb" по умолчанию

    # Проверяем, что сообщение начинается с одного из разрешенных префиксов
   for prefix in user_prefixes + command_prefixes:
      if message.text.startswith(prefix + " инфо"):

        try:
            if message.reply_message:
                user_id = message.reply_message.from_id
            else:
                user_id = message.from_id

            user_info = await api.users.get(
                user_ids=user_id,
                fields=['online', 'last_seen', 'photo_max', 'screen_name', 'sex', 'city', 'bdate', 'music', 'video', 'followers_count', 'is_closed', 'counters']
            )

            user_data = user_info[0]
            user_name = f"{user_data.first_name} {user_data.last_name}"
            user_screen_name = user_data.screen_name
            user_sex = get_gender_string(user_data.sex)
            user_city = user_data.city
            user_city_title = user_city.title if user_city else 'Город не указан'
            user_bdate = user_data.bdate if 'bdate' in user_data else 'Нет данных'

            if hasattr(user_data.counters, 'videos'):
                user_video_count = user_data.counters.videos
            else:
                user_video_count = 'Нет данных'

            if hasattr(user_data.counters, 'photos'):
                user_photos_count = user_data.counters.photos
            else:
                user_photos_count = 'Нет данных'

            if hasattr(user_data.counters, 'friends'):
                friends_count = user_data.counters.friends
            else:
                friends_count = 'Нет данных'
                
            user_info = await api.users.get(
                user_ids=user_id,
                fields=['activity', 'counters', 'followers_count', 'last_seen'],
            )
            user_data = user_info[0]

            user_status = getattr(user_data, 'activity', 'Нет данных о статусе')

            sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

            if sticker_packs_count == 0:
                counters = user_data.counters
                sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0

            # Проверяем, есть ли информация о подарках
            if hasattr(counters, 'gifts') and counters.gifts is not None:
                gifts_count = counters.gifts
            else:
                gifts_count = 'Информация о подарках скрыта.'

            followers_count = getattr(user_data, 'followers_count', 'Нет данных')

            last_seen = user_data.last_seen
            if user_data.online:
                online_status = "🟢 Онлайн"
                if last_seen and last_seen.platform:
                    online_device = last_seen.platform
                    if online_device == 1:
                        device_name = "с мобильного 📱"
                    elif online_device == 2:
                        device_name = "с iPhone 📱"
                    elif online_device == 3:
                        device_name = "с компьютера 🖥️"
                    else:
                        device_name = "с неизвестного устройства 📵"
                    online_status += f" {device_name}"
                last_seen_str = ""
            else:
                online_status = "🔴 Оффлайн"
                if last_seen and last_seen.time:
                    last_seen_time = datetime.utcfromtimestamp(last_seen.time)
                    now = datetime.utcnow()
                    time_difference = now - last_seen_time
                    last_seen_str = (
                        f"в сети: {last_seen_time.strftime('%Y-%m-%d %H:%M:%S')} "
                        f"├─ {format_timedelta(time_difference)} назад"
                    )
                else:
                    last_seen_str = "Был в сети давно"

            sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

            if sticker_packs_count == 0:
                counters = user_data.counters
                sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0

                    
            bot_info = await api.users.get(
                user_ids=message.from_id
            )
            bot_data = bot_info[0]
            bot_id = bot_data.id

            is_bot_connected = user_id == bot_id
            

            response = requests.get(f'https://vk.com/foaf.php?id={user_id}')
            xml = response.text
            soup = BeautifulSoup(xml, 'lxml')
            created = soup.find('ya:created').get('dc:date')

            created_date = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S%z")
            formatted_created_date = created_date.strftime("%Y.%m.%d в %H:%M мск")

            response = requests.get(f'https://vk.com/foaf.php?id={user_id}')
            xml = response.text
            soup = BeautifulSoup(xml, 'lxml')
            created = soup.find('ya:created').get('dc:date')

            created_date = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S%z")
            created_date = created_date.replace(tzinfo=None)

            delta = relativedelta(datetime.now(), created_date)
            total_days = delta.years * 365 + delta.months * 30 + delta.days

            account_age = format_account_age(delta)

            response_message = f"⚙ Информация о {user_name} :\n\n"
            
            response_message += f"🀄 ID: {user_id}\n"
            response_message += f"🕉 Ссылка: {user_screen_name}\n"
            response_message += f"\n🈺 Подписчики: {user_data.followers_count - friends_count if user_data.followers_count is not None else 'Нет данных'}\n"

            response_message += f"\n※ Тип Профиля: {'Закрытый' if user_data.is_closed else 'Открытый'}\n"
            response_message += f"※ Количество друзей: {friends_count}\n"

            response_message += f"\n🪪 Пол: {user_sex}\n"
            response_message += f"🌁 Город: {user_city_title}\n"

            response_message += f"\n※ Видео: {user_video_count}\n"
            response_message += f"※ Количество фотографий: {user_photos_count}\n"

            response_message += f"\n※ Дата регистрации: {formatted_created_date}\n"
            response_message += f"※ Аккаунту: {account_age} ({total_days} дней {delta.hours} часов).\n"
            response_message += f"※ Статус:\n‹‹\n{user_status}\n———››\n"

            response_message += f"\n🎁 Подарки: {gifts_count}\n"

            response_message += f"\n⩐ GB: {'✅' if is_bot_connected else '✖️'}\n"


            try:
                photo_info = await api.photos.get(
                    owner_id=user_id,
                    album_id='profile',
                    rev=1,
                    count=1,
                    photo_sizes=1,
                )
                
                if photo_info.count > 0:
                    random_id = int(time.time() * 1000)
                    attachment = [f"photo{photo_info.items[0].owner_id}_{photo_info.items[0].id}"]
                else:
                    attachment = []
                
            except VKAPIError as e:
                if "This profile is private" in str(e):
                    attachment = []
                else:
                    raise

            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=response_message,
                attachment=attachment, 
            )
            
        except VKAPIError as e:
            if "This profile is private" in str(e):
                response_message = "Профиль пользователя является приватным, и некоторая информация недоступна."
                await api.messages.send(
                    peer_id=message.peer_id,
                    message=response_message
                )
            else:
                await message.answer(f"Произошла ошибка VK API: {e}")


################################################################################




@user.on.message(text=["<prefix> пинг"])
async def ping_pong(message: Message, prefix):
    user_prefixes = load_prefixes().get(str(message.from_id), [])
    default_prefixes = ["gb", "гб"]

    if prefix.lower() in user_prefixes + default_prefixes: 
    
     if message.from_id == YOUR_USER_ID:       
        current_time = datetime.now()
        response_time = (current_time - datetime.fromtimestamp(message.date)).total_seconds()

        response_text = (
            f' Сообщение прочитано За {response_time:.2f} секунд.\n'
            f' Отправлено За {response_time * 5:.2f} секунд.\n'
            f' Отредактировано За {response_time * 2:.2f} секунд.\n'
            f' Удалено За {response_time * 3:.2f} секунд. '
        )
        
        await api.messages.edit(
            peer_id=message.peer_id,
            conversation_message_id=message.conversation_message_id,
            message=response_text
        )
################################################################################

@user.on.message(text=['<prefix> айди'])
async def check_user_id(message: Message, prefix):
    user_id = None

    if message.from_id == MAIN_ID:
        user_prefixes = load_prefixes().get(str(message.from_id), [])
        default_prefixes = ["gb", "гб"]
        
        if prefix and prefix.lower() in user_prefixes + default_prefixes:
           
            if message.reply_message:
                user_id = message.reply_message.from_id
                user_link = f"[id{user_id}|id данного пользователя ]"
            else:
                user_id = message.from_id
                user_link = f"[id{user_id}|Хозяин, Ваш id ]"

    if user_id:
        response_message = f"{user_link} : {user_id}"
        await api.messages.edit(
            peer_id=message.peer_id,
            conversation_message_id=message.conversation_message_id,
            message=response_message
        )
    else:
        await message.answer("Айди пользователя не найдено")
        


@user.on.message(text=['<prefix> проверь айди'])
async def check_user_id(message: Message, prefix):
    user_id = None

    if message.from_id == MAIN_ID:
        user_prefixes = load_prefixes().get(str(message.from_id), [])
        default_prefixes = ["gb", "гб"]
        
        if prefix and prefix.lower() in user_prefixes + default_prefixes:
           
            if message.reply_message:
                user_id = message.reply_message.from_id
                user_link = f"[id{user_id}|id данного пользователя ]"
            else:
                user_id = message.from_id
                user_link = f"[id{user_id}|Хозяин, Ваш id ]"

    if user_id:
        response_message = f"{user_link} : {user_id}"
        await api.messages.edit(
            peer_id=message.peer_id,
            conversation_message_id=message.conversation_message_id,
            message=response_message
        )
    else:
        await message.answer("Айди пользователя не найдено")

##################################################################################



@user.on.message(text="gb проверка")
async def check_user_chats(message: Message):
    if message.from_id != YOUR_USER_ID:
        return

    # Получаем ID пользователя, с которым нужно проверить беседы
    if message.reply_message:
        other_user_id = message.reply_message.from_id
    else:
        await message.answer("Пожалуйста, ответьте на сообщение пользователя, чтобы проверить его беседы.")
        return

    try:
        # Получаем список бесед, в которых состоит текущий пользователь
        response = await bp.api.messages.getConversations(count=200)
        current_user_chats = response.items

        # Проверяем, состоит ли указанный пользователь в этих беседах
        common_chats = []
        for chat in current_user_chats:
            chat_id = chat.peer_id
            chat_info = await bp.api.messages.getConversationById(conversation_ids=chat_id)
            
            if chat_info.conversations[0].chat_settings.users:
                members = chat_info.conversations[0].chat_settings.users
                if other_user_id in members:
                    common_chats.append(chat_id)

        # Формируем ответ
        if common_chats:
            response_message = "Вот список бесед, в которых вы оба находитесь:\n"
            for chat_id in common_chats:
                response_message += f"Чат ID: {chat_id}\n"
        else:
            response_message = "Вы не состоите в общих беседах с этим пользователем."

        await message.answer(response_message)

    except VKAPIError as e:
        await message.answer(f"Произошла ошибка VK API: {e}")

########################################################################################

@user.on.message(text=["<prefix> реши <expression>"])
async def solve_expression(message: Message, expression, prefix: str):
    user_prefixes = load_prefixes().get(str(message.from_id), [])
    default_prefixes = ["gb", "гб"]

    if prefix.lower() in user_prefixes + default_prefixes:    


     if message.from_id == MAIN_ID:
        try:
            expression = expression.replace("^", "**")
            
            result = eval(expression)
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=f"🧮 Результат: {result}"
            )
        except Exception as e:
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message="Ошибка: Неверное выражение"
            )

########################################################################################
            
@user.on.message(text=["<prefix> реши уравнения <equation>"])
async def примеры(message: Message, equation, prefix: str):
    user_prefixes = load_prefixes().get(str(message.from_id), [])
    default_prefixes = ["gb", "гб"]

    if prefix.lower() in user_prefixes + default_prefixes: 
    
     if message.from_id == MAIN_ID:
        try:
            # Заменяем символы для степени
            equation = equation.replace("^", "**")

            # Создаем символы для уравнения
            x = symbols('x')

            # Преобразуем строку уравнения в объект SymPy
            equation_sympy = Eq(eval(equation.replace("–", "-")), 0)

            # Решаем уравнение
            solutions = solve(equation_sympy, x)

            # Формируем ответ
            result_str = "🔢 Решения уравнения:"
            for i, solution in enumerate(solutions):
                result_str += f"\n{x} = {solution}"

            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=result_str
            )
        except Exception as e:
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message="Ошибка: Неверное уравнение или нет решений"
            )

########################################################################################            



@user.on.message(text='<prefix> переведи')
async def translate_text(message: Message, prefix):
   if message.from_id == MAIN_ID:
    user_prefixes = load_prefixes().get(str(message.from_id), [])
    default_prefixes = ["gb", "гб"]

   if prefix.lower() in user_prefixes + default_prefixes: 
   
    try:
        text_to_translate = ""


        if message.reply_message and message.reply_message.text:
            text_to_translate = message.reply_message.text
        else:

            match = re.search(r'gb переведи (.+)', message.text)
            if match:
                text_to_translate = match.group(1)

        if text_to_translate:

            source_lang = 'ru' if re.search('[а-яА-Я]', text_to_translate) else 'en'
            target_lang = 'en' if source_lang == 'ru' else 'ru'

            translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang)

            response_message = f"Перевод текста:\n{translated_text.text}"
        else:
            response_message = "Укажите текст для перевода после команды 'gb переведи' или ответьте на сообщение с текстом для перевода."


        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=response_message
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при переводе текста: {str(e)}") 
        
   user_prefixes = []   


@user.on.message(text='<prefix> перевод <text>')
async def translate_text(message: Message, text, prefix: str):
    main_id = MAIN_ID  
    if message.from_id == MAIN_ID:
        user_prefixes = load_prefixes().get(str(main_id), [])
        default_prefixes = ["gb", "гб"]

    if message.from_id == main_id and prefix.lower() in user_prefixes + default_prefixes:
   
   
        try:
            random_id = random.getrandbits(31)        
            source_lang = 'ru' if re.search('[а-яА-Я]', text) else 'en'
            target_lang = 'en' if source_lang == 'ru' else 'ru'
            translated_text = translator.translate(text, src=source_lang, dest=target_lang)
            response_message = f"Перевод текста:\n{translated_text.text}"     
            await api.messages.delete(message_ids=message.id, delete_for_all=0)  
      
            sent_message = await api.messages.send(
                peer_id=message.peer_id,
                message=response_message,
                random_id=random_id  
            )
        except Exception as e:
            await message.answer(f"Произошла ошибка: {e}")

######################################################################################################
@user.on.message(text="gb список")
async def cвs(message: Message):
    if message.reply_message:
        text = message.reply_message.text
    else:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="ты лох"
        )
        return
    items = re.split(r',\s*(?![^()]*\))', text)
    numbered_list = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])
    numbered_list = re.sub(r'([^\.])$', r'\1.', numbered_list, flags=re.MULTILINE)

    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=numbered_list
    )

######################################################################################################

COOLDOWN_DURATION = 5
last_response_time = {}
@user.on.message(text=["Яра"])
async def яра(message: Message):
    user_id = str(message.from_id)
    if user_id not in last_response_time or (
        datetime.now() - last_response_time[user_id]
    ) > timedelta(seconds=COOLDOWN_DURATION):
        last_response_time[user_id] = datetime.now()
        sticker_ids = [93905, 93953, 93858, 92924, 91087, 94355, 93174, 87171, 91746, 6310, 92326]
        random_sticker_id = random.choice(sticker_ids)
        await api.messages.send(
                peer_id=message.peer_id,
                random_id=0,
                sticker_id=random_sticker_id
            )

######################################################################################################

#############################################################################################################################################
@user.on.message(text="gb мегапуш <name>")
async def megapush(message: Message, name: str):
    if message.from_id == YOUR_USER_ID:
        chat_members = await user.api.messages.get_conversation_members(peer_id=message.peer_id)
        tag_message = message.text.split("гей", 1)[-1].strip()

        mentions = []

        for member in chat_members.items:
           
            if member.member_id > 0: 
                mentions.append(f"[id{member.member_id}|{name}]")
                
        result_message = f"{', '.join(mentions)}. {tag_message}"
        max_message_length = 4096  
        message_parts = [result_message[i:i + max_message_length] for i in range(0, len(result_message), max_message_length)]
        for i, part in enumerate(message_parts, 1):
            await user.api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=part
            )


#######################
            

@user.on.message(text="gb пуш <name>")
async def online_push(message: Message, name: str):
    if message.from_id == YOUR_USER_ID:
        chat_info = await user.api.messages.get_conversations_by_id(peer_ids=message.peer_id, extended=1)
        
        if chat_info.items:
            chat = chat_info.items[0]    
            chat_id = chat.peer.id
            chat_members = await user.api.messages.get_conversation_members(peer_id=chat_id)
          
            online_mentions = []
            for member in chat_members.profiles:
                if member.online:
                    online_mentions.append(f"[id{member.id}|{name}]")

            if online_mentions:
                mentions_str = ", ".join(online_mentions)
                await user.api.messages.edit(
                    peer_id=message.peer_id,
                    conversation_message_id=message.conversation_message_id,
                    message=mentions_str + "."
                )
            else:
                await user.api.messages.edit(
                    peer_id=message.peer_id,
                    conversation_message_id=message.conversation_message_id,
                    message=f"Нет онлайн-участников для упоминания."
                )
        else:
            await user.api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=f"Информация о беседе отсутствует."
            )
            
##############################################################################################################################################
            
@user.on.message(text=['gb дд <count:int>'])
async def delete_own_messages(message: Message, count: int):
   if message.from_id == MAIN_ID:
    peer_id = message.peer_id

    user_id = message.from_id

    if count <= 0:
        return

    message_history = await api.messages.get_history(peer_id=peer_id, count=200)
    message_ids_to_delete = []
    deleted_messages_count = 0

    for msg in message_history.items:
        if msg.from_id == user_id:
            message_ids_to_delete.append(str(msg.id))
            deleted_messages_count += 1

        if deleted_messages_count >= count:
            break

    if not message_ids_to_delete:
        return

    try:
        await api.messages.delete(message_ids=",".join(message_ids_to_delete), delete_for_all=1)
    except VKAPIError as e:
        if "Access denied" in str(e):
            pass  

@user.on.message(text=['gb дд333'])
async def delete_previous_own_messages(message: Message):
   if message.from_id == MAIN_ID:
    user_id = message.from_id
    message_history = await api.messages.get_history(peer_id=message.peer_id, count=3)

    if len(message_history.items) == 3:
        if message_history.items[0].from_id == user_id:
            await api.messages.delete(message_ids=message_history.items[0].id, delete_for_all=1)

###############################################################################################################################################

@user.on.message(text='gb +чс')
async def add_to_blacklist(message: Message):
    if message.from_id == MAIN_ID:
        user_prefixes = []  
        if message.reply_message:

            user_id = message.reply_message.from_id
            banned_users = await user.api.account.get_banned()
            user_info = await user.api.users.get(user_ids=user_id)
            user_data = user_info[0]
            user_name = f"[id{user_data.id}|{user_data.first_name} {user_data.last_name}]"
            if user_id not in banned_users:
                try:
                    await user.api.account.ban(owner_id=user_id)
                    notification_message = "Вы были добавлены в черный список."
                    await user.api.messages.send(user_id=user_id, message=notification_message)

                    await user.api.messages.edit(
                        peer_id=message.peer_id,
                        conversation_message_id=message.conversation_message_id,
                        message=f"{user_name} успешно добавлен(а) в черный список."
                    )
                except VKAPIError as e:
                    error_message = f"Произошла ошибка VK API при добавлении пользователя в черный список: {e}"
                    await message.answer(error_message)
            else:
                already_in_blacklist_message = f"{user_name} уже находится в вашем черном списке."
                await message.answer(already_in_blacklist_message)
        elif 'gb +чс' in message.text:
            import re
            mention_pattern = r'\[id(\d+)\|[^]]+\]'
            mentioned_users = re.findall(mention_pattern, message.text)
            for user_id in mentioned_users:
                try:
                    await user.api.account.ban(owner_id=int(user_id))
                    notification_message = "Вы были добавлены в черный список бота."
                    await user.api.messages.send(user_id=int(user_id), message=notification_message)
                except VKAPIError as e:
                    error_message = f"Произошла ошибка VK API при добавлении пользователя в черный список: {e}"
                    await message.answer(error_message)

#############################################################################################################################################
                                  
@user.on.message(text=['gb сот <text>'])
async def send_to_chat(message: Message, text: str):
    chat_id = -205747591

    try:
        random_id = get_random_id()

        if message.reply_message:
            response_message_id = await user.api.messages.send(peer_id=chat_id, message=text, random_id=random_id, forward_messages=[message.reply_message.id])
        else:
            response_message_id = await user.api.messages.send(peer_id=chat_id, message=text, random_id=random_id)   
        await asyncio.sleep(5)
        history = await user.api.messages.get_history(peer_id=chat_id, count=1)

        if history.items:
            response_message_id = history.items[0].id
        else:
            response_message_id = None


        if response_message_id:
            await user.api.messages.send(peer_id=message.peer_id, message='', random_id=get_random_id(), forward_messages=[response_message_id])
    except Exception as e:
        await message.answer(f"Произошла ошибка VK API: {e}")





@user.on.message(text=['gb су <text>'])
async def send_to_chat(message: Message, text: str):
    chat_id = -219622329
    user_prefixes = []  
    try:
        random_id = get_random_id()

        if message.reply_message:
            response_message_id = await user.api.messages.send(peer_id=chat_id, message=text, random_id=random_id, forward_messages=[message.reply_message.id])
        else:
            response_message_id = await user.api.messages.send(peer_id=chat_id, message=text, random_id=random_id)
        await asyncio.sleep(1)
        history = await user.api.messages.get_history(peer_id=chat_id, count=1)

        if history.items:
            response_message_id = history.items[0].id
        else:
            response_message_id = None


        if response_message_id:
            await user.api.messages.send(peer_id=message.peer_id, message='', random_id=get_random_id(), forward_messages=[response_message_id])
    except Exception as e:
        await message.answer(f"Произошла ошибка VK API: {e}")

#############################################################################################################################################
        
async def добавить_пользователя(message: Message, target: str = ""):
    if message.from_id == MAIN_ID:  # Проверяем, что команду выполняет администратор
        # Удаление сообщения с командой, если оно было ответом
        if message.reply_message:
            await api.messages.delete(message_ids=[message.id], delete_for_all=1)

        # Определяем ID пользователя для добавления
        target_id = None
        if message.reply_message:
            target_id = message.reply_message.from_id
        elif target.startswith("[id"):
            target_id = int(target.split('|')[0][3:])
        elif target.isdigit():
            target_id = int(target)

        if target_id:
            try:
                # Получаем информацию о пользователе
                user_info = await api.users.get(user_ids=target_id)
                user_data = user_info[0]
                user_name = f"[id{user_data.id}|{user_data.first_name} {user_data.last_name}]"

                # Выполняем команду добавления
                await api.messages.add_chat_user(chat_id=message.peer_id - 2000000000, user_id=target_id)
                await message.answer(f"Пользователь {user_name} был добавлен в беседу.")
            except VKAPIError as e:
                await message.answer(f"Произошла ошибка при попытке добавить пользователя: {e}")
        else:
            # Удаление сообщения, если команда была вызвана без параметров
            await api.messages.delete(message_ids=[message.id], delete_for_all=1)


        

@user.on.message(text=["gb кик <target>", "гб кик <target>", "<ваш_префикс> кик <target>"])
async def kick_user(message: Message, target: str):
    
    if message.from_id == MAIN_ID: 
        if message.reply_message:
            await api.messages.delete(message_ids=[message.id], delete_for_all=1)
            
        target_id = None
        if message.reply_message:
            target_id = message.reply_message.from_id
        elif target.startswith("[id"):
            target_id = int(target.split('|')[0][3:])
        elif target.isdigit():
            target_id = int(target)

        if target_id:
            try:
                user_info = await api.users.get(user_ids=target_id)
                user_data = user_info[0]
                user_name = f"[id{user_data.id}|{user_data.first_name} {user_data.last_name}]"

                await api.messages.remove_chat_user(chat_id=message.peer_id - 2000000000, user_id=target_id)
                await message.answer(f"Чушпан {user_name} был исключен из беседы.")
            except VKAPIError as e:
                await message.answer(f"Произошла ошибка при попытке исключить пользователя: {e}")
        else:
            await api.messages.delete(message_ids=[message.id], delete_for_all=1)

##############################################################################################################################################
            
@user.on.message(text='gb +др')
async def add_friend(message: Message):
    if message.from_id == MAIN_ID:
        if message.reply_message:
            user_id = message.reply_message.from_id
            import random
            random_id = random.getrandbits(31) 

            friend_status = await api.friends.are_friends(user_ids=[user_id])

            if friend_status and friend_status[0].friend_status == 3:
                try:
                    await api.friends.add(user_id=user_id, random_id=random_id)
                    success_message = f"Заявка на добавление в друзья от [id{user_id}|Пользователя] успешно принята."
                    await api.messages.send(
                        peer_id=message.peer_id,
                        message=success_message,
                        random_id=random_id
                    )
                except VKAPIError as e:
                    error_message = f"Произошла ошибка VK API при принятии заявки на добавление в друзья: {e}"
                    await api.messages.send(
                        peer_id=message.peer_id,
                        message=error_message,
                        random_id=random_id
                    )
            else:
                try:
                    await api.friends.add(user_id=user_id, random_id=random_id)
                    success_message = f"Заявка на добавление в друзья от [id{user_id}|Пользователя] успешно отправлена."
                    await api.messages.send(
                        peer_id=message.peer_id,
                        message=success_message,
                        random_id=random_id
                    )
                except VKAPIError as e:
                    error_message = f"Произошла ошибка VK API при отправке заявки на добавление в друзья: {e}"
                    await api.messages.send(
                        peer_id=message.peer_id,
                        message=error_message,
                        random_id=random_id
                    )
        else:
            await api.messages.delete(message_ids=[message.id])

##############################################################################################################################################
@user.on.message(text='gb -др')
async def remove_friend(message: Message):
   if message.from_id == MAIN_ID:
    if message.reply_message:
        user_id = message.reply_message.from_id
        friend_status = await api.friends.are_friends(user_ids=[user_id])

        if friend_status and friend_status[0].friend_status != 3:
            not_friend_message = f"Пользователь [id{user_id}|id{user_id}] не находится в вашем списке друзей."
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=not_friend_message
            )
        else:
            try:
                await api.friends.delete(user_id=user_id)
                success_message = f"Пользователь [id{user_id}|id{user_id}] успешно удален из друзей."
                await api.messages.edit(
                    peer_id=message.peer_id,
                    conversation_message_id=message.conversation_message_id,
                    message=success_message
                )
            except VKAPIError as e:
                error_message = f"Произошла ошибка VK API при удалении пользователя: {e}"
                await api.messages.edit(
                    peer_id=message.peer_id,
                    conversation_message_id=message.conversation_message_id,
                    message=error_message
                )
    else:
        await api.messages.delete(message_ids=[message.id])   

##############################################################################################################################################



# Функция для получения строкового представления пола
def get_gender_string(sex):
    if sex == 1:
        return 'Женский'
    elif sex == 2:
        return 'Мужской'
    else:
        return 'Не указан'

def format_account_age(delta):
    years, months, days = delta.years, delta.months, delta.days
    hours = delta.hours

    if days == 1:
        days_text = "1 день"
    elif days % 10 in {2, 3, 4} and days not in {12, 13, 14}:
        days_text = f"{days} дня"
    else:
        days_text = f"{days} дней"

    if hours == 1:
        hours_text = "1 час"
    elif hours % 10 in {2, 3, 4} and hours not in {12, 13, 14}:
        hours_text = f"{hours} часа"
    else:
        hours_text = f"{hours} часов"

    years_text = f"{years} {'год' if years == 1 else 'года' if 2 <= years <= 4 else 'лет'}"
    months_text = f"{months} {'месяц' if months == 1 else 'месяца' if 2 <= months <= 4 else 'месяцев'}"

    age_text = f"{years_text} {months_text} {days_text}."

    return age_text

def format_timedelta(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        return f"{days} дней {hours} часов {minutes} минут"
    elif hours > 0:
        return f"{hours} часов {minutes} минут"
    elif minutes > 0:
        return f"{minutes} минут"
    else:
        return f"{seconds} секунд"

    # Обработчик команды "gb проверь айди"






@user.on.message(text=["gb инфо", "гб инфо", "<ваш_префикс> инфо"])
async def remove_trusted_33user(message: Message):
   command_prefixes = ["gb", "гб", "<ваш_префикс>"]
   if message.from_id == MAIN_ID:
 # Получаем префикс пользователя из файла
       prefixes = load_prefixes()
       user_prefixes = prefixes.get(str(message.from_id), ["gb"])  # Если префикс не установлен, используем "gb" по умолчанию

    # Проверяем, что сообщение начинается с одного из разрешенных префиксов
   for prefix in user_prefixes + command_prefixes:
      if message.text.startswith(prefix + " инфо"):

        try:
            if message.reply_message:
                user_id = message.reply_message.from_id
            else:
                user_id = message.from_id

            user_info = await api.users.get(
                user_ids=user_id,
                fields=['online', 'last_seen', 'photo_max', 'screen_name', 'sex', 'city', 'bdate', 'music', 'video', 'followers_count', 'is_closed', 'counters']
            )

            user_data = user_info[0]
            user_name = f"{user_data.first_name} {user_data.last_name}"
            user_screen_name = user_data.screen_name
            user_sex = get_gender_string(user_data.sex)
            user_city = user_data.city
            user_city_title = user_city.title if user_city else 'Город не указан'
            user_bdate = user_data.bdate if 'bdate' in user_data else 'Нет данных'

            if hasattr(user_data.counters, 'videos'):
                user_video_count = user_data.counters.videos
            else:
                user_video_count = 'Нет данных'

            if hasattr(user_data.counters, 'photos'):
                user_photos_count = user_data.counters.photos
            else:
                user_photos_count = 'Нет данных'

            if hasattr(user_data.counters, 'friends'):
                friends_count = user_data.counters.friends
            else:
                friends_count = 'Нет данных'
                
            user_info = await api.users.get(
                user_ids=user_id,
                fields=['activity', 'counters', 'followers_count', 'last_seen'],
            )
            user_data = user_info[0]

            user_status = getattr(user_data, 'activity', 'Нет данных о статусе')

            sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

            if sticker_packs_count == 0:
                counters = user_data.counters
                sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0

            # Проверяем, есть ли информация о подарках
            if hasattr(counters, 'gifts') and counters.gifts is not None:
                gifts_count = counters.gifts
            else:
                gifts_count = 'Информация о подарках скрыта.'

            followers_count = getattr(user_data, 'followers_count', 'Нет данных')

            last_seen = user_data.last_seen
            if user_data.online:
                online_status = "🟢 Онлайн"
                if last_seen and last_seen.platform:
                    online_device = last_seen.platform
                    if online_device == 1:
                        device_name = "с мобильного 📱"
                    elif online_device == 2:
                        device_name = "с iPhone 📱"
                    elif online_device == 3:
                        device_name = "с компьютера 🖥️"
                    else:
                        device_name = "с неизвестного устройства 📵"
                    online_status += f" {device_name}"
                last_seen_str = ""
            else:
                online_status = "🔴 Оффлайн"
                if last_seen and last_seen.time:
                    last_seen_time = datetime.utcfromtimestamp(last_seen.time)
                    now = datetime.utcnow()
                    time_difference = now - last_seen_time
                    last_seen_str = (
                        f"в сети: {last_seen_time.strftime('%Y-%m-%d %H:%M:%S')} "
                        f"├─ {format_timedelta(time_difference)} назад"
                    )
                else:
                    last_seen_str = "Был в сети давно"

            sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

            if sticker_packs_count == 0:
                counters = user_data.counters
                sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0

                    
            bot_info = await api.users.get(
                user_ids=message.from_id
            )
            bot_data = bot_info[0]
            bot_id = bot_data.id

            is_bot_connected = user_id == bot_id
            

            response = requests.get(f'https://vk.com/foaf.php?id={user_id}')
            xml = response.text
            soup = BeautifulSoup(xml, 'lxml')
            created = soup.find('ya:created').get('dc:date')

            created_date = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S%z")
            formatted_created_date = created_date.strftime("%Y.%m.%d в %H:%M мск")

            response = requests.get(f'https://vk.com/foaf.php?id={user_id}')
            xml = response.text
            soup = BeautifulSoup(xml, 'lxml')
            created = soup.find('ya:created').get('dc:date')

            created_date = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S%z")
            created_date = created_date.replace(tzinfo=None)

            delta = relativedelta(datetime.now(), created_date) # type: ignore
            total_days = delta.years * 365 + delta.months * 30 + delta.days

            account_age = format_account_age(delta)


            response_message = f"📝 Информация о {user_name} :\n"
            response_message += f"📌 ID: {user_id}\n"
            response_message += f"🔗 Ссылка: {user_screen_name}\n"
            response_message += f"{online_status} {last_seen_str}\n"
            response_message += f"👤 Подписчики: {user_data.followers_count - friends_count if user_data.followers_count is not None else 'Нет данных'}\n"
            response_message += f"💼 Тип Профиля: {'Закрытый' if user_data.is_closed else 'Открытый'}\n"
            response_message += f"👥 Количество друзей: {friends_count}\n"
            response_message += f"⚤  Пол: {user_sex}\n"
            response_message += f"🌇 Город: {user_city_title}\n"
            response_message += f"🎬 Видео: {user_video_count}\n"
            response_message += f"📸 Количество фотографий: {user_photos_count}\n"
            response_message += f"📅 Дата регистрации: {formatted_created_date}\n"
            response_message += f"⏳ Аккаунту: {account_age} ({total_days} дней {delta.hours} часов).\n"
            response_message += f"🔸 Статус:\n{user_status}\n"
            response_message += f"🎁 Подарки: {gifts_count}\n"
            response_message += f"🎁 Количество стикеров: {sticker_packs_count}\n"
            response_message += f"                                             \n"
            response_message += f"👨🏻‍💻 GB: {'✅' if is_bot_connected else '✖️'}\n"
          
            try:
                photo_info = await api.photos.get(
                    owner_id=user_id,
                    album_id='profile',
                    rev=1,
                    count=1,
                    photo_sizes=1,
                )
                
                if photo_info.count > 0:
                    random_id = int(time.time() * 1000)
                    attachment = [f"photo{photo_info.items[0].owner_id}_{photo_info.items[0].id}"]
                else:
                    attachment = []
                
            except VKAPIError as e:
                if "This profile is private" in str(e):
                    attachment = []
                else:
                    raise

            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=response_message,
                attachment=attachment, 
            )
            
        except VKAPIError as e:
            if "This profile is private" in str(e):
                response_message = "Профиль пользователя является приватным, и некоторая информация недоступна."
                await api.messages.send(
                    peer_id=message.peer_id,
                    message=response_message
                )
            else:
                await message.answer(f"Произошла ошибка VK API: {e}")


# Загрузка префиксов из файла
def load_prefixes():
    try:
        with open("prefixes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Сохранение префиксов в файл
def save_prefixes(prefixes):
    with open("prefixes.json", "w") as file:
        json.dump(prefixes, file)


@user.on.message(text="gb +преф <prefix>")
async def add_prefix(message: Message, prefix: Optional[str]):
    print("Add prefix command received")  
    if not prefix:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="Укажите префикс, который вы хотите добавить."
        )
        return

    if prefix.lower() in ["gb", "гб"]:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=f"Префикс {prefix} является базовым и не может быть изменен."
        )
        return

    prefixes = load_prefixes()
    user_prefixes = prefixes.get(str(message.from_id), [])  

    if prefix.lower() not in map(str.lower, user_prefixes):  
        user_prefixes.append(prefix.lower())  
        prefixes[str(message.from_id)] = user_prefixes
        save_prefixes(prefixes)

        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=f"Префикс успешно добавлен: {prefix}"
        )
    else:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=f"Префикс {prefix} уже установлен."
        )


@user.on.message(text="gb преф <index>")
async def set_custom_prefix(message: Message, index: Optional[str]):
    if index is None:
        # Ваш код обработки ошибки
        return

    prefixes = load_prefixes()
    user_prefixes = prefixes.get(str(message.from_id), [])  # Получаем список префиксов пользователя

    try:
        index = int(index)  # Преобразование строки в целое число
    except ValueError:
        # Ваш код обработки ошибки
        return

    if 1 <= index <= len(user_prefixes):
        selected_prefix = user_prefixes[index - 1]
        prefixes[str(message.from_id)] = [selected_prefix.lower()]  # Устанавливаем выбранный префикс (в нижнем регистре) как текущий
        save_prefixes(prefixes)

        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=f"Префикс: {selected_prefix} Успешно установлен."
        )
    else:
        # Ваш код обработки ошибки
        return

@user.on.message(text=["gb префы"])
async def show_prefixes(message: Message):
    if message.from_id == MAIN_ID: 
        prefixes = load_prefixes()
        user_prefixes = prefixes.get(str(message.from_id), ["gb"])  
        trusted_users = load_trusted_users()  
        if message.from_id == YOUR_USER_ID and any(message.text.lower().startswith(prefix.lower()) for prefix in user_prefixes + ["gb"]):  
            prefixes = load_prefixes()
            user_prefixes = prefixes.get(str(message.from_id), [])  

    if not user_prefixes:
        response = "У вас нет установленных префиксов."
    else:
        response = "Ваши личные префиксы:\n" + "\n".join([f"{index + 1}. {prefix}" for index, prefix in enumerate(user_prefixes) if prefix.lower() not in ["gb", "гб"]])

    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=response
    )




@user.on.message(text=["gb -префы", "gb -префы"])
async def clear_prefixes(message: Message):
    prefixes = load_prefixes()
    user_prefixes = prefixes.get(str(message.from_id), ["gb"])  
    if message.from_id == YOUR_USER_ID and any(message.text.lower().startswith(prefix.lower()) for prefix in user_prefixes + ["gb"]):
     prefixes = load_prefixes()
    user_id = str(message.from_id)

    if user_id in prefixes:
        del prefixes[user_id]  # Удаляем все префиксы пользователя
        save_prefixes(prefixes)

        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="Ваши префиксы успешно очищены."
        )
    else:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="У вас нет установленных префиксов."
        )



# Обработчик команды "преф" и "префикс"

async def show_current_prefix(user, message: Message):
    prefixes = load_prefixes()
    user_prefixes = prefixes.get(str(message.from_id), ["gb"])

    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=f"⚠ Хозяин ваш Префикс: {user_prefixes[0]}"
    )
    
# Обработчик команды "gb -преф <index>"
@user.on.message(text="gb -преф <index>")
async def remove_prefix(message: Message, index: Optional[str]):
    if index is None:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="Пожалуйста, укажите номер префикса, который вы хотите удалить."
        )
        return

    prefixes = load_prefixes()
    user_prefixes = prefixes.get(str(message.from_id), [])  # Получаем список префиксов пользователя

    try:
        index = int(index)  # Преобразование строки в целое число
    except ValueError:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="Некорректный номер префикса. Пожалуйста, укажите целое число."
        )
        return

    if 1 <= index <= len(user_prefixes):
        removed_prefix = user_prefixes.pop(index - 1)  # Удаляем выбранный префикс из списка
        prefixes[str(message.from_id)] = user_prefixes
        save_prefixes(prefixes)

        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=f"Префикс успешно удален: {removed_prefix}"
        )
    else:
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message="Неправильный номер префикса. Пожалуйста, укажите существующий номер."
        )



        # Обработчик команды "gb проверь айди"
@user.on.message(text=['gb проверь айди'])
async def check_user_id(message: Message):
    if message.reply_message:
        # Получаем айди отправителя сообщения, на которое был дан ответ
        user_id = message.reply_message.from_id
        user_link = f"[id{user_id}|id данного пользователя ]"
    else:
        # Если нет ответа на сообщение, получаем ваш айди
        user_id = message.from_id
        user_link = f"[id{user_id}|Ваш id ]"

    if user_id:
        # Сообщение с айди и ссылкой
        response_message = f"{user_link} : {user_id}"
        
        # Редактирование исходящего сообщения с ответом
        await api.messages.edit(
            peer_id=message.peer_id,
            conversation_message_id=message.conversation_message_id,
            message=response_message
        )
    else:
        # Айди пользователя не найдено
        await message.answer("Айди пользователя не найдено")
        
# Обработчик команды "реши"
@user.on.message(text=["gb реши <expression>"])
async def solve_expression(message: Message, expression: str):
    # Проверка на айдишник
    if message.from_id == MAIN_ID:
        try:
            # Вычисление результата математического выражения
            result = eval(expression)
            # Редактирование исходящего сообщения с результатом
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=f"Результат = {result}"
            )
        except Exception as e:
            # Редактирование исходящего сообщения с сообщением об ошибке
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message="Ошибка: Неверное выражение"
            )
           
# Обработчик команды "gb пинг"
@user.on.message(text=['gb пинг'])
async def ping_pong(message: Message):
    # Получаем текущую дату и время
    current_time = datetime.now()
    # Вычисляем разницу во времени между отправленным сообщением и текущим временем
    response_time = (current_time - datetime.fromtimestamp(message.date)).total_seconds()
    
    # Формируем текст ответа
    response_text = f'Пинг бота: {response_time:.2f} секунд'
    
    # Редактируем исходное сообщение с ответом
    await api.messages.edit(
        peer_id=message.peer_id,
        conversation_message_id=message.conversation_message_id,
        message=response_text
    )
    
# Функция для преобразования числового значения пола в строку
def get_gender_string(gender):
    if gender == 1:
        return "женский"
    elif gender == 2:
        return "мужской"
    else:
        return "не указан"
    
# Создайте словарь, чтобы сопоставить числовые значения устройства с их описаниями
device_descriptions = {
    1: "с мобильного",
    2: "с iPhone",
    3: "с iPad",
    4: "с Android",
    5: "с Windows Phone",
    6: "с Windows 10",
    7: "с ПК",
    8: "с VK Mobile"
   } 
# Функция для получения строкового представления пола
def get_gender_string(sex):
    if sex == 1:
        return 'Женский'
    elif sex == 2:
        return 'Мужской'
    else:
        return 'Не указан'

        
# Обработчик команды "gb профиль"
@user.on.message(text='gb профиль')
async def get_user_profile(message: Message):
    try:
        if message.reply_message:
            user_id = message.reply_message.from_id
        else:
            user_id = message.from_id

        # Получение информации о пользователе, включая город и дату рождения
        user_info = await api.users.get(
            user_ids=user_id,
            fields=['online', 'last_seen', 'photo_max', 'screen_name', 'sex', 'city', 'bdate', 'music', 'videos', 'followers_count', 'is_closed', 'counters']
        )

        user_data = user_info[0]
        user_name = f"{user_data.first_name} {user_data.last_name}"
        user_id = user_data.id
        user_link = f"https://vk.com/{user_data.screen_name}"
        user_sex = get_gender_string(user_data.sex)  # Преобразование числового значения пола в строку
        user_city = user_data.city.title if 'city' in user_data else 'Нет данных'  # Город
        user_bdate = user_data.bdate if 'bdate' in user_data else 'Нет данных'  # Дата рождения
        user_music_count = user_data.music.count if 'music' in user_data else 'Нет данных'  # Количество музыки
        user_video_count = user_data.videos.count if 'videos' in user_data else 'Нет данных'  # Количество видео

        # Получение количества фотографий пользователя
        user_photos_count = user_data.counters.photos

        # Извлечение даты создания страницы пользователя
        response = requests.get(f'https://vk.com/foaf.php?id={user_id}')
        xml = response.text
        soup = BeautifulSoup(xml, 'lxml')
        created = soup.find('ya:created').get('dc:date')

        # Форматирование даты создания в нужный формат
        created_date = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S%z")
        formatted_created_date = created_date.strftime("%Y.%m.%d в %H:%M мск")

        # Получение списка друзей пользователя
        friends_info = await api.friends.get(user_id=user_id)

        # Получаем количество друзей
        friends_count = friends_info.count
        # Получаем количество подписчиков
        followers_count = user_data.followers_count

        # Определение устройства, с которого пользователь онлайн
        online_device = "📵"
        if user_data.online:
            if user_data.online_mobile:
                online_device = "📱"
            else:
                online_device = "🖥️"

        # Формирование сообщения с дополнительной информацией
        response_message = "Информация о пользователе:\n"
        response_message += f"📌 ID: {user_id}\n"
        response_message += f"🔗 Ссылка: {user_link}\n"
        response_message += f"🌐 Онлайн: {'Да' if user_data.online else 'Нет'} {online_device}\n"
        response_message += f"👤 Подписчики: {followers_count - friends_count if followers_count is not None else 'Нет данных'}\n"
        response_message += f"🔒 Закрытый профиль: {'Да' if user_data.is_closed else 'Нет'}\n"
        response_message += f"👥 Количество друзей: {friends_count}\n"
        response_message += f"🏳‍🌈 Пол: {user_sex}\n"
        response_message += f"🏙 Город: {user_city}\n"
        response_message += f"🎵 Музыки: {user_music_count}\n"
        response_message += f"📺 Видео: {user_video_count}\n"
        response_message += f"📆 Дата рождения: {user_bdate}\n"
        response_message += f"📸 Количество фотографий: {user_photos_count}\n"  # Добавляем информацию о количестве фотографий
        response_message += f"📆 Дата регистрации: {formatted_created_date}\n"

        await api.messages.edit(
            peer_id=message.peer_id,
            conversation_message_id=message.conversation_message_id,
            message=response_message
        )
    except VKAPIError as e:
        await message.answer(f"Произошла ошибка VK API: {e}")

        
        
        
        
        
        
        
        
# Обработчик команды "gb переведи"
@user.on.message(text='gb переведи')
async def translate_text(message: Message):
    try:
        text_to_translate = ""

        # Если есть ответ на сообщение, получаем текст для перевода
        if message.reply_message and message.reply_message.text:
            text_to_translate = message.reply_message.text
        else:
            # Попробуем найти текст после команды
            match = re.search(r'gb переведи (.+)', message.text)
            if match:
                text_to_translate = match.group(1)

        if text_to_translate:
            # Определяем исходный и целевой язык для перевода
            source_lang = 'ru' if re.search('[а-яА-Я]', text_to_translate) else 'en'
            target_lang = 'en' if source_lang == 'ru' else 'ru'

            # Переводим текст
            translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang)

            response_message = f"Перевод текста:\n{translated_text.text}"
        else:
            response_message = "Укажите текст для перевода после команды 'gb переведи' или ответьте на сообщение с текстом для перевода."

        # Редактируем оригинальное сообщение с ответом
        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message.id,
            message=response_message
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при переводе текста: {str(e)}") 
        
        
        
        
        
        

        

                        



        


#запуск бота
logger.debug('________________\n')
logger.debug(' СТАРТ ГБ')
logger.debug('________________')
user.run_forever()













