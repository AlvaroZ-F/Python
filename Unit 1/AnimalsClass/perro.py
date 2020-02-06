from flyer import Flyer 

class Dog(Flyer):
    def __init__(self, name, moving, flying=False, height=int(0), crash=False):
        self.moving = moving
        self.name = name
        self.flying = flying
        self.height = height
        self.crash = crash

    def __str__(self):
        return "The dog is named "+name

    def __dir__(self):
        dog_atr = [str(Atr_name_String), str(Met_talk())]
        return dog_atr

    def talk():
        return "Woof!"
