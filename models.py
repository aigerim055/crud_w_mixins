from utils import Id

class Cars:
    def __init__(self, mark, car_model,year_of_issue, engine_volume, color, type, mileage, price):
        self.id = Id().id_
        self.mark = mark
        self.car_model =  car_model
        self.year_of_issue = year_of_issue
        self.engine_volume = engine_volume
        self.color = color
        self.type = type
        self.mileage = mileage
        self.price = price

   

    @property
    def as_dict(self):
        self.__dict__['year_of_issue'] =  str(self.__dict__['year_of_issue']) 
        return self.__dict__

'''
● марка (строка)
● модель (строка)
● год выпуска (целое число)
● объем двигателя (decimal, точность 1 знак)
● цвет (строка)
● тип кузова (поле одиночного выбора.
варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
● пробег (целое число)
● цена (decimal, точность 2 знака)
'''