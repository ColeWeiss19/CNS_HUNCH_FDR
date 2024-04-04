from machine import Pin, PWM
import math
import random
import time

servo1 = PWM(Pin(21))
servo2 = PWM(Pin(15))
signal = Pin(2, Pin.IN, Pin.PULL_DOWN)

def callback(signal):
    global interrupt_flag
    interrupt_flag = 1

def sweepMotion(servo, position):
    servo.duty_u16(position)
    time.sleep(0.01)

def scrubMotion(servo, position):
    servo.duty_u16(position)
    time.sleep(0.001)

signal.irq(trigger=Pin.IRQ_RISING,handler = callback)

#----- Thread 1 Code -----#
thread1 = True

def worker1(servo1):
  global thread1
  servo1.freq(50)
  while True:
      for pos in range(0, 9000, 50):
        if thread1:
          sweepMotion(servo1, pos)
      for pos in range(9000, 0, -50):
        if thread1:
          sweepMotion(servo1, pos)

thread = thread.start_new_thread(worker1, (servo1,))

#----- Thread 1 Code -----#

#----- Thread 0 Code -----#
thread0 = True

def worker2(servo2):
  servo2.freq(50)
    for pos in range(0, 9000, 50):
      if thread0:
        scrubMotion(servo2, pos)
    for pos in range(9000, 0, -50):
      if thread0:
        scrubMotion(servo2, pos)
        
    servo2.duty_u16(4500)

while True:
  worker2(servo2)
  thread0, thread1 = True
  if interrupt_flag is 1:
    thread0, thread1 = False
    interrupt_flag = 0
    time.sleep(5)

#----- Thread 0 Code -----#
