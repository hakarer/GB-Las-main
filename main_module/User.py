import asyncio

class User_ac:  
    '''ОБЪЕКТ'''
    def __init__(self):
        """Стандартные характеристики"""
        self.id = 0
        self.name = "Отсутствует"
        self.last_name = "Отсутствует"
    
    async def reg(self, id: int):
        self.id = id
        self.name = "Отсутствует"
        self.last_name = "Отсутствует"
        return self



