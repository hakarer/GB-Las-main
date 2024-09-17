import orjson
import random
from config import TOKEN,api_list
from main_module.main_function import *
from rules import From_Me,Prefix
from datetime import datetime
import time
from bs4 import BeautifulSoup
import random, requests
from dateutil.relativedelta import relativedelta
from vkbottle import VKAPIError
from vk_api.utils import get_random_id
import asyncio


math_labeler = UserLabeler()
math_labeler.vbml_ignore_case = True



@math_labeler.message(From_Me(),Prefix(),text=['<pref>реши <expression>'])
@error
async def math(message: Message, expression:str):
        try:
            expression = expression.replace("^", "**")
            
            result = eval(expression)
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message=f"🧮 Результат: {expression}={result}"
            )
        except Exception as e:
            await api.messages.edit(
                peer_id=message.peer_id,
                conversation_message_id=message.conversation_message_id,
                message="Ошибка: Неверное выражение"
            )



@math_labeler.message(From_Me(), text=['сот лс <text>'])
@error
async def Su(message: Message, text: str):
    chat_id = -205747591
    random_id = get_random_id()
    response_received = asyncio.Event()
    
    async def wait_for_response():
        await asyncio.sleep(5)
        if not response_received.is_set():
            await user.api.messages.edit(
                peer_id=message.peer_id,
                message='Сотик не ответил 😔',
                message_id=message.id
            )

    await user.api.messages.send(
        peer_id=chat_id,
        message=text,
        random_id=random_id,
        forward_messages=[message.reply_message.id] if message.reply_message else None
    )
    
    wait_task = asyncio.create_task(wait_for_response())

    while not response_received.is_set():
        history = await user.api.messages.get_history(peer_id=chat_id, count=2)
        response_message = next((item for item in history.items if item.from_id == chat_id and item.date > message.date), None)
        
        if response_message:
            await user.api.messages.send(
                peer_id=message.peer_id,
                message='',
                random_id=random_id,
                forward_messages=[response_message.id]
            )
            response_received.set()
        
        await asyncio.sleep(0.1)

    await wait_task


    
@math_labeler.message(From_Me(), text=['су лс <text>'])
@error
async def Su(message: Message, text: str):
    chat_id = -219622329
    random_id = get_random_id()
    response_received = asyncio.Event()
    
    async def wait_for_response():
        await asyncio.sleep(5)
        if not response_received.is_set():
            await user.api.messages.edit(
                peer_id=message.peer_id,
                message='Суджи не ответила',
                message_id=message.id
            )

    await user.api.messages.send(
        peer_id=chat_id,
        message=text,
        random_id=random_id,
        forward_messages=[message.reply_message.id] if message.reply_message else None
    )
    
    wait_task = asyncio.create_task(wait_for_response())

    while not response_received.is_set():
        history = await user.api.messages.get_history(peer_id=chat_id, count=2)
        response_message = next((item for item in history.items if item.from_id == chat_id and item.date > message.date), None)
        
        if response_message:
            await user.api.messages.send(
                peer_id=message.peer_id,
                message='',
                random_id=random_id,
                forward_messages=[response_message.id]
            )
            response_received.set()
        
        await asyncio.sleep(0.1)

    await wait_task
