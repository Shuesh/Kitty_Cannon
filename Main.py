import opencv


#Waiting state. No face detected. Reset to homing position
def standby:


#Manual override. Replaces track, verify, and delay functions
def manual:


#Target has been acquired. Runs a PID loop as a background process that always moves servos to 
def track:


#Verify that the crosshairs are close enough to being on target that we should shoot
def verify:


#Shoot sprayer, delay if in auto mode, go back to verify
def shoot:


#If not in manual operation, use the config value to delay between shots
def delay:


