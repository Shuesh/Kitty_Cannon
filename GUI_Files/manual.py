import gpio_interface
import time

class control_state(object):
    
    def __init__(self, azimuth = 45, elevation = 45):
        self.azimuth = azimuth
        self.elevation = elevation

        self.pi = gpio_interface.pi_board()


    def move_up(self, amount):
        self.elevation = self.pi.get_elevation()
        if self.elevation < 220:
            self.pi.set_elevation(self.elevation + amount)

    def move_down(self, amount):
        self.elevation = self.pi.get_elevation()
        if self.azimuth > 40:
            self.pi.set_elevation(self.elevation - amount)


    def move_left(self, amount):
        self.azimuth = self.pi.get_azimuth()
        if self.azimuth > 40:
            self.pi.set_azimuth(self.azimuth - amount)

    def move_right(self, amount):
        self.azimuth = self.pi.get_azimuth()
        if self.azimuth < 220:
            self.pi.set_azimuth(self.azimuth + amount)


    def fire(self):
        pass



if __name__ == '__main__':
    control = control_state()
    for _ in range(0,45):
        control.move_left(2)
        time.sleep(0.05)