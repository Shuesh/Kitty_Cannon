import rpi.gpio as gpio

#Start in the center of the servo range on bootup
gpio.setmode(gpio.board)
gpio.setup(11, gpio.out)

p = gpio.pwm(11,50)
pwm = 7.5
p.start(pwm)
