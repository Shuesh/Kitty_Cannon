import pigpio as io

#Start in the center of the servo range on bootup
io.setmode(gpio.board)
io.setup(11, gpio.out)

p = gpio.pwm(11,50)
pwm = 7.5
p.start(pwm)
