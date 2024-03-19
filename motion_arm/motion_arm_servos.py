#Randomized Servos for Grabber

from machine import Pin, PWM
import math
import random

servo = PWM(Pin(1))
servo.freq(50)

def randomMotion(servo):
    randomRadian = (((math.pi/2) * random.randint(-100, 100)))/100
    position = (randomRadian * (180/math.pi)) * 50
    servo.duty_u16(position)

# To set the servo to a neutral position:
#--- servo.duty_u16(4500) ---#
