import json 


class JsonMixin:
    '''класс для записи в json файл'''
    def get_db_content(self):
        try:
            with open(self._file_name, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'cars': [], 'counter' : 0}


    def write_to_db(self, data):
        with open(self._file_name, 'w') as file:
            json.dump(data, file, indent=4)


class Create:
    '''класс для создания записей'''
    def create(self):
        try:
            mark = input('введите название марки машины: ')
            car_model = input('введите название модели машины: ')
            year_of_issue = int(input('введите год выпуска машины: '))
            engine_volume = float(input('ведите объем двигателя: '))
            color = input('введите цвет машины: ')
            type = input('введите тип кузова(варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ')
            mileage = int(input('введите пробег машины: '))
            price = float(input('введите цену машины в долларах: '))
            model = self._model(mark=mark, car_model=car_model, year_of_issue=year_of_issue, engine_volume=engine_volume, color=color, mileage=mileage, 
            price=price, type=type)
            data = self.get_db_content()
            data['cars'].append(model.as_dict)
            data.update(counter=len(data['cars']))
            self.write_to_db(data)
            print('*'*35)
            print('машина добавлена успешно!'.upper())
            print('*'*35)
        except ValueError:
            print('!'*35)
            print('не правильный ввод данных, попробуйте снова')
            print('!'*35)


class Read:
    '''класс для чтения записи'''
    def list(self):
        data = self.get_db_content()
        print('-'*35)
        for i in data['cars']:
            for k, v in i.items():
                print(f'{k}: {v}')
            print('-'*35)
        
    

    def get_user_by_id(self):
        self.show_all_id()
        user_id = input('enter id: ')
        data = self.get_db_content()
        car = data['cars']
        res = list(filter(lambda x: x['id'] == user_id, car))
        print('-'*35)
        for i in res:
            for k, v in i.items():
                print(f'{k}: {v}')
            print('-'*35)
        return res[0] if res else None

    def show_all_id(self):
        all_id = self.get_db_content()
        print('доступные id:')
        for id in all_id['cars']:
            print(id['id'])
            print(' ')


class Update:
    """обновляет данные записи"""
    def update(self):
        model = self._model 

        data = self.get_db_content()
        car = self.get_user_by_id()
        
        
        try:
            if car is not None:
                data['cars'].remove(car)
                mark = input('введите новое название марки машины: ') or car['mark']
                car_model = input('введите новое название модели машины: ') or car['car_model']
                year_of_issue = int(input('введите год выпуска машины: ')) or car['year_of_issue']
                engine_volume = float(input('ведите объем двигателя: ')) or car['engine_volume']
                color = input('введите цвет машины: ') or car['color']
                type = input('введите тип кузова(варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ') or car['type']
                mileage = int(input('введите пробег машины: ')) or car['mieage']
                price = float(input('введите цену машины в долларах: ')) or car['price']
                new_model = self._model(mark=mark, car_model=car_model, year_of_issue=year_of_issue, engine_volume=engine_volume, color=color, mileage=mileage, 
                price=price, type=type)
                new_model.__dict__['id'] = car['id']
                data['cars'].append(new_model.as_dict)
                self.write_to_db(data)
                print('*'*35)
                print('успешно обновлено!'.upper())
                print('*'*35)            
            else:
                print('dont find')
        except ValueError:
            print('!'*35)
            print('заполнитяйте поле ввода!')
            print('!'*35)

class Delete:
    """удаляет запись"""
    def delete(self):
        data = self.get_db_content()
        car = self.get_user_by_id()

        
        if car is not None:
            data['cars'].remove(car)
            data.update(counter=len(data['cars']))

            self.write_to_db(data)

            print('успешно удален!')
        else:
            print('dont find')