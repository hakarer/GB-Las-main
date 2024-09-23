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


profile_labeler = UserLabeler()
profile_labeler.vbml_ignore_case = True

# Функция для получения строкового представления пола
async def get_gender_string(sex):
    if sex == 1:
        return '💋 Пол: Женский'
    elif sex == 2:
        return '🍌 Пол: Мужской'
    else:
        return '❓ Пол: Не указан'

async def format_account_age(delta):
    years, months, days = delta.years, delta.months, delta.days
    hours = delta.hours

    if days == 1:
        days_text = "1 д."
    elif days % 10 in {2, 3, 4} and days not in {12, 13, 14}:
        days_text = f"{days} д."
    else:
        days_text = f"{days} дн."

    if hours == 1:
        hours_text = "1 ч."
    elif hours % 10 in {2, 3, 4} and hours not in {12, 13, 14}:
        hours_text = f"{hours} ч."
    else:
        hours_text = f"{hours} ч."

    years_text = f"{years} {'г.' if years == 1 else 'г.' if 2 <= years <= 4 else 'г.'}"
    months_text = f"{months} {'мес.' if months == 1 else 'мес.' if 2 <= months <= 4 else 'мес.'}"

    age_text = f"{years_text} {months_text} {days_text}"

    return age_text

async def format_timedelta(delta):
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




        
@profile_labeler.message(From_Me(), Prefix(), text=['<pref>+др', '<pref>+др <link>'])
async def manage_friends(message: Message, link: str = None):
    user_id = message.reply_message.from_id if message.reply_message else await get_id(message=message, text=link)
    if not user_id:
        return await mess_new(message=message, text="⚠ ID пользователя не найдено.", red=True)
    try:
        random_id = random.getrandbits(31)
        user_info = await api.users.get(user_ids=user_id)
        user_name = f"{user_info[0].first_name} {user_info[0].last_name}"
        friend_status = (await api.friends.are_friends(user_ids=[user_id]))[0].friend_status

        if friend_status == 3:
            await mess_new(message=message, text=f" [id{user_id}|{user_name}] уже у вас в друзьях.", red=True)
        else:
            await api.friends.add(user_id=user_id, random_id=random_id)
            if friend_status == 2:
                await mess_new(message=message, text=f"Заявка от [id{user_id}|{user_name}] принята.", red=True)
            else:
                await mess_new(message=message, text=f"Заявка в друзья [id{user_id}|{user_name}] отправлена.", red=True)
    except VKAPIError as e:
        if "blacklist" in str(e):
            await mess_new(message=message, text=f"⚠ Ошибка : [id{user_id}|{user_name}] добавил вас в чс", red=True)
        else:
            await mess_new(message=message, text=f"⚠ Ошибка: {e}", red=True)
###########################################################

@profile_labeler.message(From_Me(), Prefix(), text=['<pref>-др', '<pref>-др <link>'])
async def remove_friend(message: Message, link: str = None):
    user_id = message.reply_message.from_id if message.reply_message else await get_id(message=message, text=link)

    if not user_id:
        return await mess_new(message=message, text="⚠ ID пользователя не найдено.", red=True)

    try:
        user_info = await api.users.get(user_ids=user_id)
        user_name = f"{user_info[0].first_name} {user_info[0].last_name}"

        friend_status = (await api.friends.are_friends(user_ids=[user_id]))[0].friend_status

        if friend_status == 0:
            await mess_new(message=message, text=f"⚠ [id{user_id}|{user_name}] уже не является вашим другом.", red=True)
        elif friend_status == 3:
            await api.friends.delete(user_id=user_id)
            await mess_new(message=message, text=f"[id{user_id}|{user_name}] успешно удалён из друзей.", red=True)
        else:
            await mess_new(message=message, text=f"⚠ Невозможно удалить [id{user_id}|{user_name}] из друзей, поскольку Его(Её) заявка в друзья ждет вашего одобрения .", red=True)
    except VKAPIError as e:
        if "blacklist" in str(e):
            await mess_new(message=message, text=f"⚠ Ошибка : [id{user_id}|{user_name}] добавил вас в чс", red=True)
        else:
            await mess_new(message=message, text=f"⚠ Ошибка: {e}", red=True)
###########################################################

@profile_labeler.message(From_Me(),Prefix(),text=['<pref>айди', '<pref>айди <link>','<pref>id', '<pref>id <link>','<pref>fqlb', '<pref>fqlb <link>','<pref>шв', '<pref>шв <link>'])
@error
async def user_id_check(message: Message,link: str = None):
    
    user_id = await get_id(message=message, text=link)

    try:
        if user_id:
            await mess_new(message=message, text=f"🀄 ID Пользователя: {user_id}",red=True)
        else:
            await mess_new(message=message, text=f"⚠ ID Пользователя не найдено.",red=True)
    except:
        await mess_new(message=message, text=f"⚠ Параметры пользователя указаны не верно.",red=True)
###########################################################

@profile_labeler.message(From_Me(),Prefix(),text=['<pref>профиль','<pref>профиль <link> <link2>','<pref>инфо <link> <link2>','<pref>профиль <link>','<pref>инфо <link>','<pref>инфо',])
@error
async def profile(message: Message, link: str=None, link2: str=None):
    try:
        podr=False
        if link!=None:
            if link=="подробно":
                podr=True
                link=link2
        if link2!=None:
            if link2=="подробно":
                podr=True


        user_id = await get_id(message=message, text=link)
        user_info = await user.api.users.get(
            user_ids=user_id,
            fields=['bdate',
                    'online',
                    'last_seen',
                    'photo_max',
                    'screen_name',
                    'sex',
                    'city',
                    'music',
                    'video',
                    'followers_count',
                    'is_closed',
                    'counters']
        )



        user_data = user_info[0]
        user_name = f"{user_data.first_name} {user_data.last_name}"
        user_screen_name = user_data.screen_name
        user_sex = await get_gender_string(user_data.sex)
        user_city = user_data.city
        user_city_title = user_city.title if user_city else 'Не указан'
        try:
            user_bdate = user_data.bdate
            if user_bdate == None:
                user_bdate = "Скрыто"
        except:
            user_bdate = 'Скрыто'

        if hasattr(user_data.counters, 'videos'):
            user_video_count = user_data.counters.videos
        else:
            user_video_count = 'Скрыто'

        if hasattr(user_data.counters, 'photos'):
            user_photos_count = user_data.counters.photos
        else:
            user_photos_count = 'Скрыто'

        if hasattr(user_data.counters, 'friends'):
            friends_count = user_data.counters.friends
        else:
            friends_count = 'Скрыто'
            
        user_info = await api.users.get(
            user_ids=user_id,
            fields=['activity', 'counters', 'followers_count', 'last_seen'],
        )
        user_data = user_info[0]

        user_status = getattr(user_data, 'activity', 'Скрыто о статусе')

        sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

        if sticker_packs_count == 0:
            counters = user_data.counters
            sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0

        # Проверяем, есть ли информация о подарках
        if hasattr(counters, 'gifts') and counters.gifts is not None:
            gifts_count = counters.gifts
        else:
            gifts_count = 'Скрыты.'

        followers_count = getattr(user_data, 'followers_count', 'Скрыто')

        # last_seen = user_data.last_seen
        # if user_data.online:
        #     online_status = "🟢 Онлайн"
        #     if last_seen and last_seen.platform:
        #         online_device = last_seen.platform
        #         if online_device == 1:
        #             device_name = "Андроид 📱"
        #         elif online_device == 2:
        #             device_name = "iPhone 📱"
        #         elif online_device == 3:
        #             device_name = "ПК 🖥️"
        #         else:
        #             device_name = " Неизвестно 📵"
        #         online_status += f" {device_name}"
        #     last_seen_str = ""
        # else:
        #     online_status = "🔴 Оффлайн"
        #     if last_seen and last_seen.time:
        #         last_seen_time = datetime.utcfromtimestamp(last_seen.time)
        #         now = datetime.utcnow()
        #         time_difference = now - last_seen_time
        #         last_seen_str = (
        #             f"в сети: {last_seen_time.strftime('%Y-%m-%d %H:%M:%S')} "
        #             f"├─ {await format_timedelta(time_difference)} назад"
        #         )
        #     else:
        #         last_seen_str = "Был в сети давно"

        # sticker_packs_count = user_data.activity.stickers if hasattr(user_data.activity, 'stickers') else 0

        # if sticker_packs_count == 0:
        #     counters = user_data.counters
        #     sticker_packs_count = counters.sticker_packs if hasattr(counters, 'sticker_packs') else 0


        

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

        account_age = await format_account_age(delta)

        params = {
                'user_id':user_id,
                'type': "stickers",
                'filters':['purchased'],
                }  
        
        response = await api.request("store.getProducts",params)
        response=response['response']
        count=response['count']

        if podr:
            response_message=(
                f"⚙ Профиль @id0({user_name}):\n\n"

                f"{'🔒  Профиль: Закрытый' if user_data.is_closed else '🔓 Профиль: Открытый'}\n"
                f"🀄 ID: {user_id}\n"
                f"🕉 Тэг: @{user_screen_name}\n\n"
                

                f"🍼 День рождения: {user_bdate}\n"
                f"{user_sex}\n"
                f"🌏 Город: {user_city_title}\n\n"

                f"🫧 Друзья: {friends_count}\n"
                f"🧿 Подписчики: {user_data.followers_count - friends_count if user_data.followers_count is not None else 'Скрыто'}\n"

                f"🎬 Видео: {user_video_count}\n"
                f"🏞 Фото: {user_photos_count}\n"
                f"🎁 Подарки: {gifts_count}\n"
                f"💠 Стикеры: {count}\n\n"

                f"🗓️ Регистрация: {formatted_created_date}\n"
                f"⏳ Аккаунту: {account_age} \n"
                f"🕒 ({total_days} дней  {delta.hours} часов).\n\n"
                
                f"{'' if user_status=='' else f'💭 Статус: «{user_status}»'}"
            )
        else:
            response_message=(
                f"⚙ Профиль @id0({user_name}):\n"
                f"🕉 Тэг: @{user_screen_name}\n\n"
                

                f"🍼 День рождения: {user_bdate}\n"
                f"{user_sex}\n"
                f"🌏 Город: {user_city_title}\n\n"

                f"🫧 Друзья: {friends_count}\n"
                f"🧿 Подписчики: {user_data.followers_count - friends_count if user_data.followers_count is not None else 'Скрыто'}\n"

                f"🎁 Подарки: {gifts_count}\n"
                f"💠 Стикеры: {count}\n\n"

                f"🗓️ Регистрация: {formatted_created_date}\n"
            )

        
        

        



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
        

        await mess_new(message=message,text=response_message,red=True,attachment=attachment)
        
    except VKAPIError as e:
        if "This profile is private" in str(e):
            response_message = "Профиль пользователя является приватным, и некоторая информация недоступна."
            await api.messages.send(
                peer_id=message.peer_id,
                message=response_message
            )
###########################################################

@profile_labeler.message(From_Me(),Prefix(),text=['<pref>стики','<pref>стики <link>'])
@error
async def profile(message: Message, link: str=None, link2: str=None):
        
        user_id = await get_id(message=message, text=link)
        user_info = await user.api.users.get( user_ids=user_id)

        user_data = user_info[0]

        user_name = f"{user_data.first_name}"

        Sticker_list={}

        params = {
                'user_id': user_id,
                'type': "stickers",
                'filters':['purchased'],
                }  
        
        response = await api.request("store.getProducts",params)
        response=response['response']
        count=response['count']
        StickerPacks=response['items']
        for sticker_pack in StickerPacks:
            Sticker_list[sticker_pack['id']]=sticker_pack['purchase_date']
        await sticker_loader(StickerPacks)

        sort_dict= dict(sorted((value, key) for (key,value) in Sticker_list.items()))
        i=0
        while (list(sort_dict.keys()))[i]==0:
            i+=1
        first_sticker =sticker_info[(list(sort_dict.values()))[i]]['name']
        last_sticker =sticker_info[(list(sort_dict.values()))[len(sort_dict)-1]]['name']
        
        (buy_count,free_count,unical_count,
        anim_count,style_count,money,love_author,love_author_count)=await SticerPack.stick_stats(StickerPacks)
        text=(
            f"👁‍🗨 @id{user_id}({user_name}) имеет {count} стикер-паков\n\n"

            f"💷 Платные паки: {buy_count}\n"
            f"🎁 Бесплатные паки: {free_count}\n"
            f"💎 Уникальные паки: {unical_count}\n\n"

            f"💠 Анимированные паки: {anim_count}\n"
            f"🎭 Стили для паков:  {style_count}\n"
            f"👨‍🎨 Любимый автор: {love_author} ({love_author_count})\n\n"

            f"🔶 Первый полученный пак: {first_sticker}\n"
            f"🔷 Последний полученный пак: {last_sticker}\n\n"

            f"🐩 Цена в голосах: {money}\n"
            f"👑 Цена в рублях: {money*7} ₽\n"
        )

        await mess_new(message=message,text=text,red=True)
###########################################################

class SticerPack:
    '''ОБЪЕКТ'''

    def __init__(self):
        self.id=0
        self.name=''
        self.autor=''
        self.price=0

        self.free=False
        self.unic=False
        self.don=False

        self.anim=False
        self.style=False
    

    async def stick_stats(items):
        stic_list=[]
        for sticker_pack in items:
            stic_list.append(sticker_pack['id'])

        buy_count=0
        free_count=0
        unical_count=0
        anim_count=0
        style_count=0
        money=0
        author_dict={}
        for x in stic_list:
            dict_stic=sticker_info[x]
            try:
                if dict_stic['don']:
                    buy_count+=1  
            except:
                 pass
            try:
                if dict_stic['free']:
                    free_count+=1 
            except:
                 pass
            try:
                if dict_stic['unic']:
                    unical_count+=1 
            except:
                 pass
            try:
                if dict_stic['anim']:
                    anim_count+=1 
            except:
                 pass
            try:
                if dict_stic['style']:
                    style_count+=1 
            except:
                 pass
            money+=dict_stic['price']
            if dict_stic['author'] in list(author_dict.keys()):
                author_dict[dict_stic['author']]+=1
            else: author_dict[dict_stic['author']]=1


        
        sort_dict= dict(sorted((value, key) for (key,value) in author_dict.items()))
        love_author=(list(sort_dict.values()))[len(sort_dict)-1]
        love_author_count=author_dict[love_author]
        return (buy_count,free_count,unical_count,
                anim_count,style_count,money,love_author,love_author_count)
            
"""Подгрузка стикеров"""
async def sticker_loader(items):
        global sticker_info
        stick_api = API(token=TOKEN)  
        stic_list=[]
        for sticker_pack in items:
            if sticker_pack['id'] in list(sticker_info.keys()):
                pass
            else:
                stic_list.append(sticker_pack['id'])
        
        if stic_list==[]:
            return
        i=0
        f=300
        StickerPacks=[]
        while i<=len(items):
            if f>=len(items):
                f=len(items)
            params = {
                'type': "stickers",
                'product_ids':stic_list[i:f],
                # 'extended':True,
                }  
            if stic_list[i:f]==[]:
                break
            while True:
                try:
                    response = await stick_api.request("store.getStockItems",params)
                    break
                except:
                    stick_api=await apichange()
            response=response['response']
            StickerPacks+=response['items']


            if i+300>len(items):
                break
            i+=300
            if i+300>=len(items):
                f=len(items)
            else:
                f+=300
        for sticker_pack in StickerPacks:
            product=sticker_pack['product']
            name=product['title']
            author=sticker_pack['author']

            price=0

            free=False
            unic=False
            don=False

            if "free" in list(sticker_pack.keys()):
                if sticker_pack["free"]==1:
                    free=True
                    pass
                else:
                    if "old_price" in list(sticker_pack.keys()):
                        price=sticker_pack["old_price"]
                    elif "price" in list(sticker_pack.keys()):
                        price=sticker_pack["price"]
                    elif "price_buy" in list(sticker_pack.keys()):
                        price=sticker_pack["price_buy"]
                    if "price_str" in list(sticker_pack.keys()):
                        if sticker_pack['price_str']=='Бесплатно':
                            free=True
                            
            else:
                if "old_price" in list(sticker_pack.keys()):
                    price=sticker_pack["old_price"]
                elif "price" in list(sticker_pack.keys()):
                    price=sticker_pack["price"]
                elif "price_buy" in list(sticker_pack.keys()):
                    price=sticker_pack["price_buy"]
                if "price_str" in list(sticker_pack.keys()):
                    if sticker_pack['price_str']=='Бесплатно':
                        free=True

            if free==False and price>0:
                don=True
            elif free==False and price==0:
                unic=True
            
            # if free==False and price==0:
            #     if sticker_pack['purchase_details']['text']=='Его нельзя купить, но\xa0он может выпасть при\xa0покупке случайного набора стикеров в\xa0мобильном приложении\xa0— в\xa0рамках акции «Мне повезёт!» до\xa015.03.2025. Правила: vk.cc/cgzIZ3.':
            #         unic=True
            #     else:
            #         free=True
            

            sticker_info[product['id']]={
                'name':name,
                'author':author,
                'price':price,
                'free':free,
                'unic':unic,
                'don':don
                }
            
        i=0
        f=300
        StickerPacks=[]
        while i<=len(items):
            if f>=len(items):
                f=len(items)
            params = {
                'type': "stickers",
                'product_ids':stic_list[i:f],
                'extended':True,
                }  
            if stic_list[i:f]==[]:
                break
            while True:
                try:
                    response = await stick_api.request("store.getProducts",params)
                    break
                except:
                    stick_api=apichange()

            response=response['response']
            StickerPacks+=response['items']


            if i+300>len(items):
                break
            i+=300
            if i+300>=len(items):
                f=len(items)
            else:
                f+=300
        
        for sticker_pack in StickerPacks:
            anim=False
            style=False
            if "has_animation" in list(sticker_pack.keys()):
                if sticker_pack['has_animation']==1:
                    anim=True
            if "style_sticker_ids" in list(sticker_pack.keys()):
                    style=True

            (sticker_info[sticker_pack['id']])['anim']=anim
            (sticker_info[sticker_pack['id']])['style']=style
        
        return

sticker_info={}

async def apichange():
    try:
        global api_num
        aps=api_list[api_num]
        api_num+=1
        if api_num >= len(api_list):
                api_num=0
        return aps
    except:
        pass