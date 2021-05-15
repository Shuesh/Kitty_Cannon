import opencv
import RPi.GPIO as gpio

from config import config

#Waiting state. No face detected. Reset to homing position
def standby:


#Manual override. Replaces track, verify, and delay functions
def manual:


#Target has been acquired. Runs a PID loop as a background process that always moves servos to aim
def track (Kp, Ki, Kd, MV_bar=0):
    #Initialize stored data
    e_prev = 0
    t_prev = -100
    I = 0

    #Initial control
    MV = MV_bar

    while True:
        #yield MV, wait for new t, PV, SP
        t, PV, SP = yield MV

        #PID calculations
        e = SP - PV

        P = Kp*e
        I = I + Ki*e*(t - t_prev)
        D = Kd*(e - e_prev)/(t - t_prev)

        MV = MV_bar + P + I + D

        #Update stored data for next iteration
        e_prev = e
        t_prev = t

#Verify that the crosshairs are close enough to being on target that we should shoot
def verify:


#Shoot sprayer, delay if in auto mode, go back to verify
def shoot:


#If not in manual operation, use the config value to delay between shots
def delay:


