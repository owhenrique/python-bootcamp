import datetime

class Entity:
    def __init__(self, id):
        self.__id = id
        self.createdAt = datetime.datetime.now().isoformat()
        self.createdAt = datetime.datetime.now().isoformat()

    def getId(self):
        return self.__id