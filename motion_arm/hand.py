#360-degree servo code

from sensor import *

servo = PWM(Pin(0)) # setting the Pin to PWM

#------------------#
#time.sleep_ms(2000) # optional for delay before starting
#------------------#

def closeHand(servo):

    servo.duty_u16(9000) # setting the servo to max speed in + direction

    time.sleep_ms(1550) # delay for 1.55 seconds

    servo.duty_u16(0) # stopping servo

def openHand(servo):
    
    servo.duty_u16(50) # setting the servo to max speed in - direction

    time.sleep_ms(1550) # delay for 1.55 seconds

    servo.duty_u16(0) # stopping servo
    
def readAndClose(servo):
    
    if search() == True:
        closeHand(servo)
    
def reset():
    
    openHand(servo)
    
    calibrate(data())
