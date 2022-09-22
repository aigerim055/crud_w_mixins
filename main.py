from models import Cars
from mixins import JsonMixin,Create, Read, Update, Delete




class Main(JsonMixin,Create, Read, Update, Delete):
    _model = Cars
    _file_name = 'db.json'


    def command_list(self):
        print('список комманд которые вы можете совершить:')
        print(
            '''
            ● create - создание записи
            ● listing - получение списка записи
            ● retrieve - получение одной записи
            ● update - обновление записи
            ● delete - удаления записи
            ● exit - выйти из программы
            ● help - список комманд
            ''')

    def start(self):
        commands = {
            'create': self.create,
            'listing': self.list,
            'retrieve': self.get_user_by_id,
            'update': self.update,
            'delete': self.delete,
            'help': self.command_list
        }
        self.command_list()
        while True:
            command = input('введите команду: ').lower().strip()
            if command in commands:
                commands[command]()
            elif command == 'exit':
                print('GOODBYE:)')
                break
            elif command == 'help':
               self.command_list()

            else:
                print('!'*35)
                print('такой команды нету!'.upper())
                print('!'*35)


car = Main()
car.start()
