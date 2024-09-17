import orjson
import random
from config import TOKEN
from main_module.main_function import *
from rules import From_Me,Prefix


pres_bet_labeler = UserLabeler()
pres_bet_labeler.vbml_ignore_case = True

"""Проверка включения автотыканья монетки"""
pres_bet = False
"""Максимальная ставка"""
bet_max=10000
"""Минимальная ставка"""
bet_min=1000
"""Номера чато для нажатия ставок"""
pres_peer=[0]

"""Привязка монетки к чату"""
@pres_bet_labeler.message(From_Me(),Prefix(),text=['<pref>аайди','<pref>аайди <peer_id>','<pref>аайди<peer_id>'])
@error
async def pres_bet_listing(message: Message, peer_id:str=""):
    global pres_peer

    if peer_id =='+':
        if not message.peer_id in pres_peer:
            pres_peer.append(message.peer_id)
        
    elif peer_id =='-':
        if message.peer_id in pres_peer:
            pres_peer.remove(message.peer_id)
    elif peer_id == '0':
        pres_peer=[0]
    else:
        if not message.peer_id in pres_peer:
            pres_peer.append(message.peer_id)
        elif message.peer_id in pres_peer:
            pres_peer.remove(message.peer_id)
    from main_module.main_function import Main_user
    await mess_new(message=message,text=f'📋 Ваш id: {Main_user.id}',red=True)

"""Проверка подключеныз чатов"""
@pres_bet_labeler.message(From_Me(),Prefix(),text=['<pref>монетка лист','<pref>мл'])
@error
async def pres_bet_list_checing(message: Message, peer_id:str="",):
    if pres_peer == [0]:
        text = (
        "📋 Авто Монетка доступна во всех чатах!\n\n"
    )
    else:
        text = (
        "📋 Список чатов подключеных к автомонетке:\n\n"
        )
        i=1
        for x in pres_peer:
            text+=f"{i}. {x}\n"
            i+=1
        
        text+=f"🔸 Всего чатов: {i} \n"

    await mess_new(message=message,text=text,red=True)

"""Установка максимальной и максимальной ставки"""
@pres_bet_labeler.message(From_Me(),Prefix(),text=['<pref>ставка <type> <sum>','<pref> монетка ставка <type> <sum>'])
@error
async def pres_bet_max_min(message: Message, type:str, sum:str):
    global bet_max
    global bet_min

    if type == 'макс':
        bet_max = int(sum)
    elif type == 'мин':
        bet_min = int(sum)
    else:
       return

    await mess_new(message=message,text=f'⚔️ {type} ставка установлена.',red=True) 

"""Включение автотыка монетки"""
@pres_bet_labeler.message(From_Me(),Prefix(),text=['<pref>пресбет','<pref>автомонетка','<pref>монетка'])
@error
async def pres_bet_vkl(message: Message):
    global pres_bet

    if pres_bet: 
        pres_bet = False
        text = "❌ Монетка выкл"
    else: 
        pres_bet = True
        text = "✅ монетка вкл"

    await mess_new(message=message,text=text,red=True)

"""Настройки"""
@pres_bet_labeler.message(From_Me(),Prefix(),text=['<pref>пресбет настройки'])
@error
async def pres_bet_option(message: Message):
    global pres_bet

    text = (
        "⚙ Настройки Автомонетки:\n\n"
    )
    if pres_bet: 
        text += "✅ монетка вкл\n\n"
    else: 
        text += "❌ Монетка выкл\n\n"

    text += f"⚔️ Принимаемые ставки: {bet_min} - {bet_max}\n\n"

    text += f"📋 Подключенные чаты: "
    if pres_peer == [0]:
        text+="Все"
    else:
        text+=f"{pres_peer}"
        

    await mess_new(message=message,text=text,red=True)


@pres_bet_labeler.chat_message()
async def pres_bet_game_catch(message: Message):
    if pres_bet:
        if keyboard := message.keyboard:
            payload: dict = orjson.loads(keyboard.buttons[0][0]['action']['payload'])

            if payload.get('type') == 'coin_game':
                if message.peer_id in pres_peer or pres_peer==[0]:
                    if  payload.get('bet') <= bet_max and payload.get('bet')>= bet_min:
                        if payload.get('play_id') == 0 or payload.get('play_id') == Main_user.id:
                            st = random.choice([0,1])
                            payload_button=message.keyboard.buttons[0][st]["action"]["payload"]

                            await user.api.request('messages.sendMessageEvent', {'author_id': -205747591,'message_id': message.id,'peer_id': message.peer_id, "payload": payload_button}) 
                            logger.info(f"🪙 Тыкаю ставку {payload_button['user_id']}  на сумму {payload_button['bet']}")