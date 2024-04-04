#Randomized Servos for Grabber

from machine import Pin, PWM
import math
import random
import time

def randomMotion(servo):
    # defining servo frequency for PWM
    servo.freq(50)
    
    # creating random angles and outputting to servo
    randomRadian = (((math.pi/2) * random.randint(-100, 100)))/100
    degrees = math.ceil(randomRadian * (180/math.pi))
    position = abs(degrees * 50)
    servo.duty_u16(position)
    
    # giving the servo time to turn to the angle
    time.sleep(0.5)

# To set the servo to a neutral position:
#--- servo.duty_u16(4500) ---#
