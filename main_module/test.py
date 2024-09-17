
from main_module.main_function import *
from rules import From_Me,Prefix


test_labeler = UserLabeler()
test_labeler.vbml_ignore_case = True

"""Функция инициализация Юзера при запуске бота"""
@test_labeler.message(From_Me(),Prefix(),text=['<pref>гей <link>','<pref>гей'])
@error
async def testitos(message: Message,link:str = 0):
    message.text = await Prefix().get_text_msg(message)
    await mess_new(message=message,text=f"{message.text}\n\n{link}",red=True)

