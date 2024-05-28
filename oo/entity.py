import random
import datetime

class Entity:
    def __init__(self):
        self.id = random.randint(0, 1000000)
        self.createdAt = datetime.datetime.now().isoformat()
        self.updatedAt = datetime.datetime.now().isoformat()

    def getId(self):
        return self.id
