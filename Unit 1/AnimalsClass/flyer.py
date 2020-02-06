from animal import Animal

class Flyer(Animal):
    def __init__(self, moving, flying=False, height=int(0), crash=False):
        self.flying = flying
        self.height = height
        self.crash = crash
        self.moving = moving

    def __str__(self):
        if (flying):
            return "This animal is flying at " + str(height)+ "meters height"
        else:
            return "This animal isn't flying right now, but could"

    def __dir__(self):
        flyer_atr = [str(Atr_flying_bool), str(Atr_height_int), str(Atr_crash_bool), str(Met_take_off()), str(Met_fly_up()), str(Met_fly_down()), str(Met_land())]
        return flyer_atr

    def take_off(self):
        self.flying = True

    def fly_up(self):
        self.height += 1

    def fly_down(self):
        self.height  -= 1

    def land(self):
        self.flying = False
