class Animal:
    def __init__(self, moving=False):
        self.moving = moving

    def __str__(self):
        output = ''
        if (moving):
            output="The animal is moving"
        else:
            output="The animal isn't moving"
        return output

    def __dir__(self):
        animal_atr = [str(Atr_moving_bool),str(Met_move()). str(Met_stop())]
        return animal_art

    def move(self):
        self.moving = True

    def stop(self):
        self.moving = False
