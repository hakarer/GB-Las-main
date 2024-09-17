import random
from main_module.main_function import *
from rules import From_Me,Prefix
from data.album_list import rp_command_dicti_duo, rp_command_dicti_onli
from config import api_list

rp_labeler = UserLabeler()
rp_labeler.vbml_ignore_case = True

api_num=0   

#Получение списка участников беседы
async def member_sheck(message: Message): 
    try:
        a=await user_list_peer(message.peer_id)
        f=-1
        while f<0:
            result=random.randint(0,a.count-1)  
            f=a.items[result].member_id
    except Exception as e:
                    await message.answer(f"⚠️ Возникла ошибка {e}\n📴 Повторите попытку позднее.")  
    return f

@alru_cache(maxsize=100)
async def user_list_peer(peer_id:int):
    a=await user.api.messages.get_conversation_members(peer_id=peer_id)
    return a


#Проверка рп команды на параметр второго участника
async def rpsheck(message: Message,link: str=None):
    try:
        users_info= await register(None,f'[id{message.from_id}|')
        if message.fwd_messages:
            users_info2= await register(message.fwd_messages[0],link)
        elif link==None and message.reply_message==None:
            if message.peer_id<2000000001:
                users_info2= await register(message,f'[id{message.peer_id}|')
            else:
                users_info2= await register(message,link)
        else : 
            if message.peer_id<2000000001:
                users_info2= await register(message,f'[id{message.peer_id}|')
            else:
                if link=="рандом":
                    rnd_id=await member_sheck(message)
                    users_info2= await register(None,f'[id{rnd_id}|')
                else:
                    users_info2= await register(message,link)
        
        return [users_info,users_info2]
        
    except Exception as e:
                    await message.answer(f"⚠️ Возникла ошибка {e}\n📴 Повторите попытку позднее.")  

#Все рп команды
@rp_labeler.message(From_Me(),Prefix(),text=['<pref><link> \n<text>','<pref><link>\n<text>','<pref><link>'])
@error
async def rp_handlear(message: Message,pref:str,link:str,text: str=None):          
    link=link.lower()  
    # await message.answer(f'1\n преф |{pref}|\n линк |{link}| \n текст |{text}|')
    if link.find("[id")!=-1:
        link_text=link.find("[id")
        rp_command=link[:link_text-1]
        link=link[link_text:]
    elif link.find("@")!=-1:
        link_text=link.find("@")
        rp_command=link[:link_text-1]
        link=link[link_text:]
    elif link.find('ht')!=-1:        
        link_text=link.rfind('ht')
        rp_command=link[:link_text-1]
        link = link[link_text:]
    elif link.find('vk')!=-1:        
        link_text=link.rfind('vk')
        rp_command=link[:link_text-1]
        link = link[link_text:]
    elif link.find('рандом')!=-1:        
        link_text=link.rfind('рандом')
        rp_command=link[:link_text-1]
        link = 'рандом'
    else:
        rp_command=link
        link=None
    
    rp_command = await Prefix().get_text(rp_command)
    
    # await message.answer(f'2\nлинк |{link}| \nрп команда |{rp_command}|\n текст |{text}|')
    
    if rp_command_dicti_duo.get(rp_command)==None:
        #Одиночные рп
        if rp_command_dicti_onli.get(rp_command)==None:
            return
        else:
            if link!=None:
                return
            rp_dict=rp_command_dicti_onli.get(rp_command)
            #--------------
            users_info= await register(message,f'[id{message.from_id}|')
            pol_alb=rp_dict.get('pol_a')
            if pol_alb==None:
                album=rp_dict.get('album')  
                if users_info['sex']==1:
                    rp_text=rp_dict.get('text_M')
                elif users_info['sex']==2:
                    rp_text=rp_dict.get('text_G')
                smile=rp_dict.get('smile')
            elif pol_alb==1:
                if users_info['sex']==1:
                    rp_text=rp_dict.get('text_M')
                    album=rp_dict.get('album_M') 
                    smile=rp_dict.get('smile_M')
                elif users_info['sex']==2:
                    rp_text=rp_dict.get('text_G')
                    album=rp_dict.get('album_G') 
                    smile=rp_dict.get('smile_G')
            rp_attachment=await albom_get_function(album)
            ts=''   
            if text!=None:
                ts=f"💭 Со словами: {text}"
            tag=await tag_check(users_info)
            await mess_new(message=message, text=f"{smile}| {tag} {rp_text}\n {ts}", attachment=rp_attachment[random.randint(0,len(rp_attachment)-1)],red=True)
            # await bot.api.messages.delete(cmids=message.conversation_message_id,peer_id=message.peer_id, delete_for_all=True)
            
    else:
        #Рп на двоих
        rp_shek=await rpsheck(message,link)
        rp_dict=rp_command_dicti_duo.get(rp_command)
        #--------------
        users_info=rp_shek[0]
        users_info2=rp_shek[1]

        #Проверка альбома на разный пол
        pol_alb=rp_dict.get('pol_a')
        if pol_alb==None:
            album=rp_dict.get('album')  
        elif pol_alb==1:
            if users_info['sex']==2 and users_info2['sex']==2:
                album=rp_dict.get('album_G_G')  
            elif users_info['sex']==1 and users_info2['sex']==1:
                album=rp_dict.get('album_M_M')  
            else:
                album=rp_dict.get('album_M_G')  
        elif pol_alb==2:
            if users_info2['sex']==1:
                await message.answer((f"⚠ Данное рп-действие можно применить только к Девушкам!"),disable_mentions=1) 
                return      
            if users_info['sex']==2 and users_info2['sex']==2:
                album=rp_dict.get('album_G_G')  
            else:
                album=rp_dict.get('album_M_G') 
        elif pol_alb==3:
            if users_info2['sex']==2:
                await message.answer((f"⚠ Данное рп-действие можно применить только к Парням!"),disable_mentions=1) 
                return      
            if users_info['sex']==1 and users_info2['sex']==1:
                album=rp_dict.get('album_M_M')  
            else:
                album=rp_dict.get('album_M_G') 
        elif pol_alb==4: 
            if users_info['sex']==1:
                album=rp_dict.get('album_M')  
            else:
                album=rp_dict.get('album_G') 
        if rp_dict.get('pol_a')==None:
            album=rp_dict.get('album')  
        if users_info['sex']==1 or users_info['sex']==1:
            rp_text=rp_dict.get('text_M')
        elif users_info['sex']==2:
            rp_text=rp_dict.get('text_G')
        smile=rp_dict.get('smile')
        try:
            rp_attachment=await albom_get_function(album)
        except Exception as e:
            pass
        
        ts=''   
        if text!=None:
            ts=f"💭 Со словами: {text}"
        tag=await tag_check(users_info)
        tag2=await tag_check(users_info2)
        # await message.answer(f'6 {rp_culc}') 
        # await message.answer(f'4\n команда |{rp_command}| \n текст |{smile}| {tag} {rp_text} {tag2}\n {ts}| \n альбом |{album}| \n картинка |{rp_attachment}|')
        if rp_command=='судить'and users_info2['user_id']==DARS_ID:
            await message.answer((f"{smile}| {tag} {rp_text} лоликонщика {tag2}\n {ts}"),attachment=f"photo-{SUGI_ID}_457240255",disable_mentions=1) 
        else:    
            await mess_new(message=message, text=f"{smile}| {tag} {rp_text} {tag2}\n {ts}", attachment=rp_attachment[random.randint(0,len(rp_attachment)-1)],red=True)
            # await message.answer((f"{rp_culc}\n{smile}| {tag} {rp_text} {tag2}\n {ts}"),attachment=rp_attachment[random.randint(0,len(rp_attachment)-1)],disable_mentions=1)  
        return

#Кеширование альбомов
@alru_cache(maxsize=50)
async def albom_get_function(album_id:str):
    try:
        rp_list=[]
        global api_num
        user_api=api_list[api_num]
        album_ids=album_id.split(sep='_')
        GROUP_ID=int(album_ids[0])
        album_id=int(album_ids[1])
        n=await user_api.photos.get(owner_id=-GROUP_ID,album_id=album_id,photo_sizes=False)
        for n in n.items:
            rp_list.append(f"photo-{GROUP_ID}_{n.id}")
        api_num+=1
        if api_num>=  len(api_list):
                api_num=0
        return rp_list
    except:
        pass