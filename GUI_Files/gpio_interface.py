import pigpio
import time


class pi_board(object):

    def __init__(self, azimuth = 90, elevation = 90):
        #Initialize the pi
        self.pi = pigpio.pi()

        # GPIO 4 is physical pin 7
        self.AZIMUTH_PIN = 4
        # GPIO 27 is physical pin 13
        self.ELEVATION_PIN = 27

        # set pins to output mode
        self.pi.set_mode(self.AZIMUTH_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.ELEVATION_PIN, pigpio.OUTPUT)
        # rescale the range to 1836 so that pwm is from 40 - 220
        self.pi.set_PWM_range(self.AZIMUTH_PIN, 1836)
        self.pi.set_PWM_range(self.ELEVATION_PIN, 1836)
        # define the frequency of the periods
        self.pi.set_PWM_frequency(self.AZIMUTH_PIN, 50)
        self.pi.set_PWM_frequency(self.ELEVATION_PIN, 50)

        # Set position with the initial settings
        self.set_azimuth(azimuth)
        self.set_elevation(elevation)



    def set_azimuth(self, angle):
        # Offset the input by 40 so that we can take inputs from 0 to 180 degrees
        self.pi.set_PWM_dutycycle(self.AZIMUTH_PIN, angle + 40)


    def get_azimuth(self):
        angle = self.pi.get_PWM_dutycycle(self.AZIMUTH_PIN) - 40
        return angle

    
    def set_elevation(self, angle):
        # Offset the input by 40 so that we can take inputs from 0 to 180 degrees
        self.pi.set_PWM_dutycycle(self.ELEVATION_PIN, angle + 40)

    
    def get_elevation(self):
        angle = self.pi.get_PWM_dutycycle(self.ELEVATION_PIN) - 40
        return angle



def main():

    rpi = pi_board(90, 90)

    print(rpi.get_azimuth())
    time.sleep(1)

    rpi.set_azimuth(0)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(90)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(0)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(90)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(180)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(90)
    print(rpi.get_azimuth())
    time.sleep(1)
    rpi.set_azimuth(45)
    print(rpi.get_azimuth())
    



if __name__ == '__main__':
    main()