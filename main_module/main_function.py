from vkbottle import API,Callback, GroupEventType, GroupTypes, Text,OpenLink
from vkbottle.user import Message, UserLabeler
from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.dispatch.rules import ABCRule
from loguru import logger
import datetime
import re
from async_lru import alru_cache
import functools
from .User import User_ac
from config import api,user,sug_db,DARS_ID,SUGI_ID,SOTE_ID





main_labeler = UserLabeler()
main_labeler.vbml_ignore_case = True

Main_user=User_ac()

start = True

"""Стартовое правило при запуске бота"""
class Start_Rule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        global start
        if start == True:
            start = False
            return True
        else:
            return False


""" Отправка сообщений """ 
async def mess_new(message:Message=None,event: GroupTypes.MessageEvent=None,red:bool=None,text:str=None,attachment:str=None):
    if message!=None:
        peer_id=message.peer_id
        cmi=message.conversation_message_id
        id=message.from_id
    elif event!=None:
        peer_id=event.object.peer_id
        cmi=event.object.conversation_message_id
        id=event.object.user_id
    
    if red!=None:
        if red:
            try:
                if attachment!=None:
                    await user.api.messages.edit(
                        peer_id,
                        message=text,
                        attachment=attachment,
                        conversation_message_id=cmi,
                        disable_mentions=1) 
                else:
                    await user.api.messages.edit(
                        peer_id,
                        message=text,
                        conversation_message_id=cmi,
                        disable_mentions=1) 
            except:
                await user.api.messages.delete(cmids=cmi,peer_id=peer_id, delete_for_all=True)
                if attachment!=None:
                    await user.api.messages.send(
                        peer_id=peer_id,
                        message=text,random_id=0,
                        attachment=attachment,
                        disable_mentions=1)
                else:
                    await user.api.messages.send(
                        peer_id=peer_id,
                        message=text,random_id=0,
                        disable_mentions=1)
        else:
            if attachment!=None:
                await user.api.messages.send(
                    peer_id=peer_id,
                    message=text,random_id=0,
                    attachment=attachment,
                    disable_mentions=1)
            else:
                await user.api.messages.send(
                    peer_id=peer_id,
                    message=text,random_id=0,
                    disable_mentions=1)
    else:
        if attachment!=None:
            mes = await user.api.messages.send(
                peer_id=peer_id,
                message=text,random_id=0,
                attachment=attachment,
                disable_mentions=1)
        else:
            mes = await user.api.messages.send(
                peer_id=peer_id,
                message=text,random_id=0,
                disable_mentions=1)
            
            return mes


""" Обработчик ошибок и логирование """
def error(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        if args==():
            event=kwargs.get('event', None)
            message=kwargs.get('message', None)
        else:
            event=None
            message=args[0]
        
        try:
            logger.info(f"💻 Выполняю функцию {func.__name__}")

            await func(*args, **kwargs)
        except Exception as e:
            logger.error(f"⚠️   Ошибка {e} в функции {func.__name__} \n_______________ \n")
            logger.info(f"kwargs: {kwargs} | args:{args} ")

            logger.error(f"\n_______________ \n")
            text = f"⚠️ Возникла ошибка {e} в функции {func.__name__}\n📴 Повторите попытку позднее!"  
            if event != None:
                await mess_new(event=event, text=text, red=False)
            else:
                await mess_new(message=message, text=text)

    return wrapper


"""Функция инициализация Юзера при запуске бота"""
@main_labeler.message(Start_Rule())
@error
async def first_reg(message: Message):
    global Main_user
    user_vk_info = await user.api.users.get()
    id = user_vk_info[0].id
    Main_user = await User_ac.reg(User_ac(),id)

#ФУНКУИЯ ПОЛУЧЕНИЯ ID 1.0
async def get_id(message: Message, text) -> int:
    #ПРОВЕРКА НА КОЛЛИЧЕСТВО СЛОВ
    if text!=None:
        if text.startswith('[id')==1 or text.startswith('ht')==1 or text.startswith('vk')==1:  
            if len(re.split(' ',text))>1:
                text=re.split(' ',text)[1]
            #ПОЛУЧЕНИЕ ID
            if text.startswith('[id'):
                play_id = text[text.find("[id"):text.find("|")]
                return int(play_id[3:])
            elif text.startswith('ht') or text.startswith('vk'):        
                play_id = text[text.rfind("/")+1:]
                play_id= (await user.api.users.get(play_id))[0].id

                return play_id
            else:
                return message.from_id   
        return None
    else:
        if message.fwd_messages:
            return message.fwd_messages[0].from_id
        elif message.reply_message:
            return message.reply_message.from_id 
        else:
            return message.from_id    
#-------------------------------------------   

"""РЕГИСТРАЦИЯ"""
async def register(message: Message,link: str=None):
#ПОЛУЧЕНИЕ ID ЮЗЕРА
        try:
            id=await get_id(message,link)
        except:
            return None
        
        User = await sug_db['user'].find_one({'user_id': id})
        #ПРОВЕРКА ЮЗЕРА НА НАЛИЧИЕ В БД
        if User==None:  
            if id>0:
                users_info=await user.api.users.get(id,fields='sex')
                id=users_info[0].id
                name=users_info[0].first_name
            else:
                group_info=await user.api.groups.get_by_id(group_id=-id,fields='name')
                id=-group_info[0].id
                name=group_info[0].name       
    #-------------------------------------------       
            #ОСНОВНАЯ ЧАСТЬ
            try: 
                try:
                    if  users_info[0].sex==None:
                        sex=1
                    elif  users_info[0].sex==2:
                        sex=1
                    elif  users_info[0].sex==1:
                        sex=2
                    else:
                        sex=2  
                except:
                    sex=2
                
                User={
                'user_id': id,
                'name': name,
                'stage': '🍻Отдыхающий',
                'VIP': 0,
                'VIP_date': datetime.datetime.now() ,
                #параметры профиля 
                # 0 Скрытый, 1 баланс, 2 стата, 3 аватар, 4 снаряжение, 5 характеристикия
                'prof_option': [False,True,True,0,True,True],
                'gold': 0, 
                'b_gold':0, 
                'coin':0,
                'pers':1,
                'balans':'b_gold', 
                # 'su_gold' :0,
                'data_reg': datetime.datetime.now() ,
                'sex':sex,
                }
                #---------------
                stata={
                'user_id': id,
                'rang': '🎩 Гость',
                'vin_count': 0,
                'louse_count': 0,
                'neitral_count': 0,
                'vin_m_count': 0,
                'louse_m_count': 0,
                #---------------
                'vin_strick': 0,
                'louse_strick': 0,
                'vin_now': 0,
                'louse_now': 0,
                }
                #---------------
                User=await vip_check_end_vip(User)
                return User 
            except: 
                pass
        User=await vip_check_end_vip(User)

        return User
#-------------------------------------------   

#ФУНКУИЯ ТЕГА
async def tag_check(User):
    id=User['user_id']
    if id>0:
            tag=f"*id{id} ({User['name']})"
    else:
        tag=f"@club{-id} ({User['name']})"
    return tag
#-------------------------------------------   

#ХЕНДЛЕР ВИП ПРОВЕРКА
async def vip_check_end_vip(User):     
    if User['VIP_date']<datetime.datetime.now():
        User['VIP']=0
    return User
#------------------------------------------- 
