from machine import Pin, PWM
import math
import random
import time

servo1 = PWM(Pin(21))
servo2 = PWM(Pin(15))

servo1.freq(50)
servo2.freq(50)

def sweepMotion(servo, position):
    servo.duty_u16(position)
    time.sleep(0.01)

def scrubMotion(servo, position):
    servo.duty_u16(position)
    time.sleep(0.001)

for i in range(2):
    for pos in range(0, 9000, 50):
        sweepMotion(servo1, pos)
    for pos in range(9000, 0, -50):
        sweepMotion(servo1, pos)
        
    servo1.duty_u16(4500)

for i in range(10):
    for pos in range(0, 9000, 50):
        scrubMotion(servo2, pos)
    for pos in range(9000, 0, -50):
        scrubMotion(servo2, pos)
        
    servo2.duty_u16(4500)
