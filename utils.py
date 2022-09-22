import uuid



class Id:
    ''''класс для получения id'''
    def __init__(self) -> None:
        self._id = self.generate_id()

    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())[:8]

    @property
    def id_(self):
        return self._id
    