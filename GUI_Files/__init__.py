import rpi.gpio as gpio

gpio.setmode(gpio.board)
gpio.setup(11, gpio.out)

p = gpio.pwm(11,50)
pwm = 7.5
p.start(pwm)
