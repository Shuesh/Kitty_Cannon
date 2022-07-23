
class ControlState(object):
    #Some default starting states in case nothing has been run yet.
    #We will want manual to take over in the same place as auto, which will require some extra code.
    azimuth = 0
    elevation = 0

    def __init__(azimuth = 0, elevation = 0):
        self.azimuth = azimuth
        self.elevation = elevation


    def up(amount):
        elevation += amount


    def down(amount):
        elevation -= amount


    def left(amount):
        azimuth -= amount


    def right(amount):
        azimuth += amount


    def fire():
        pass