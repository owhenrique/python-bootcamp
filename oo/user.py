import datetime
from entity import Entity

class User(Entity):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        super().__init__()
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email

    def updateName(self, name):
        self.name = name
        self.updatedAt = datetime.datetime.now().isoformat()