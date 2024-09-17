from vkbottle import API
from vkbottle.user import User, UserLabeler
from Token import TOKEN
import motor.motor_asyncio

import motor.motor_asyncio 




SUG_BD_CONNECT='mongodb+srv://only_viev:A89-he9-JuQ-uUF@cluster0.lcxxboz.mongodb.net/?retryWrites=true&w=majority'

oretrapi = API(token="vk1.a.J1ZJ6N_YsXXM6V-m0TF6yOSpi5qW4PBkbBEAsTXD9rB2scpuGgCQTgFgD3o3YsCdmqDEStX_CJkxtH2X75JlDCa8Y6UkXTNo2Tdk-t6OWJ4S7G7Zc3NHDlop5K0E7S5gooa4-FeL73pQh1jYHbfSzTtXVmmFZWFnBQ4XLcqZcGKy1yPjkxBl4J16PctKkHXzls2QQRBOlDXK1D-YXavzoA")
springapi = API(token="vk1.a.-hAHy0zTYcCoqfknsyjwhl_8yNeF1M9DB0_JJOTJstdxf5lbe-H7FiJbycMqkTDy5tb-cD2JTPxSjLOr5agBCPZ3YSxflcDElsvOIzqPx3crIXfFCnEbbqrxziOUnW5wMfgntqDz_85-J6uhEm1klhb6OJI2y249HNZXXPtCJppHSWvWemjfv1ojcgUd4xvKblrE6zHheXrGj9DiVSdmUA")
lindaapi = API(token="vk1.a.WpQC6l6Pq56kZps7mUemkyFKIhKnIUqFAH35lHK9t1oTZb9gqp2TIgu0itWaxc0gBDaSPASgwXkvsWW6EBVQ5e8ILYy9lIyg_WLcdcBhIqyxBVhfYOyJadz-5nBf4nLQ5v_eQR-7s86gImrGBRegYm82WJU0F7iqNfU00RlqlVe1CMY8rfDuzIxDCGGCici_T-Xlv0XLYXxO1-mylY_nlA")
leonapi = API(token="vk1.a.usCcrtWcD0z2nzEEtwi0wc6HceKZ-N6_4fyMPZl1_gBmFRlQsdCW3DirwG5W44LewHs4Uhtn5G9X2pn37UdEjeZPWVylIp0umbYli4fpRNbDC5OmlTlwZ0PFMj08d54JBRTt_dGzqplKLgArEYKyHwyANj-j5Dkb8Fgn5nJ42kFJAIBxwEFy6E_I93EVqWA7LWBg_h801zgjtZvTkpC4Eg")
winslowapi = API(token="vk1.a.d-EICXLbzXDRngWepHQkaSbxEjNyrQpsihYZb6Lj-Ki931x2T5QLX_b4mqmLZweCPLqAp9oH5Sp-JCY0PL6T7zZ_wRWHfudQSnMX20Vu2-QSsV4nLYPujdHtpRfO87mAVgCJCfPSiDablB3W2hlJNsSbZUxbS9wsq4phIue29jmHOFkKmvLcbLcD_oCbipwGLoXPSEolxGHmig76pbzs6Q")
perplapi = API(token="vk1.a.gElbND9RlSjhSBAyG9hD5uCFqFn0cg7IikubMmvrWcERPQRbmfH1EJecUxT-ipEDh8_AmQw8ilCkaJ56huC2vrfes3yYM2S4sAGeMrbohtJp49tJBsj4TeSFf1eFBeilXdRcdy0IekhHLueYDRceRMgYjpLBPcdvCrPHN2ZGssveY9WzBJL0AYfWpxbVpL1o87SYwCskesYgNV34WxAPZA")

api_list=[oretrapi,springapi,lindaapi,leonapi,winslowapi,perplapi]




api=API(token=TOKEN)
user=User(api=api)

DARS_ID=528729304
SUGI_ID = 219622329
SOTE_ID = 205747591

prefixes=["gb ","loc ","гб ","лок ","лас ","!gb ","!loc ","!гб ","!лок ","!лас ","/gb ","/loc ","/гб ","/лок ","/лас ",]

labeler = UserLabeler()
user.labeler.vbml_ignore_case = True

#ПОДКЛЮЧЕНИЕ К БД
db = motor.motor_asyncio.AsyncIOMotorClient(SUG_BD_CONNECT)
sug_db = db['Kazino777']

""" https://symbl.cc/ru/tools/text-to-symbols/ генератор текста """