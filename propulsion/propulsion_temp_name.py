#randomization interfacing with motor pump

from adafruit_motorkit import MotorKit
from gpiozero import Servo
from time import sleep
from random import randint
import math

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

kit = MotorKit()

kit.motor2.throttle = 1.0
sleep(1)
kit.motor1.throttle = 1.0
sleep(12)
kit.motor1.throttle = 0

#----------------------------

servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
theta = []

for i in range(7):
    theta.append((((math.pi/2) * randint(-100, 100)))/100)

def setServoCycle(theta):
    angle = math.sin(theta)
    servo.value = angle
    #sleep(1)
    #servo.mid()

for angle in theta:
    setServoCycle(angle)
    
    kit.motor2.throttle = 0
    sleep(randint(1,2))
    kit.motor2.throttle = 1.0
    sleep(1)
    

kit.motor2.throttle = 0
sleep(20)
kit.motor2.throttle = 1.0

