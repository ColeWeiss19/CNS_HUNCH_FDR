#temporary test file

from arm_movements import *
from hand import *
import _thread as thread

#----- Thread 1 Code -----#

thread1 = True

signal = Pin(2, Pin.IN, Pin.PULL_DOWN)
servo1 = PWM(Pin(3))
servo2 = PWM(Pin(4))

interrupt_flag = 0

def callback(signal):
    global interrupt_flag
    interrupt_flag = 1

signal.irq(trigger=Pin.IRQ_RISING,handler = callback)

def worker(servo1, servo2):
    global thread1
    while True:
        if thread1:
            randomMotion(servo1)
            randomMotion(servo2)

thread = thread.start_new_thread(worker, (servo1, servo2))

#----- Thread 1 Code -----#

#----- Thread 0 Code -----#

thread0 = True

contServo = PWM(Pin(2))

touch = ADC(Pin(28))
sigVal = calibrate()

while True:
    thread0, thread1 = True, True
  if interrupt_flag is 1:
    thread0, thread1 = False, False
    interrupt_flag = 0
    time.sleep(5)
    
    # when interrupt is detected
    # stop both threads
    '''
    if interruptDetected:
        thread0, thread1 = False
    
    '''
    
    if thread0:
        if search(touch, sigVal) == True:
            print(sigVal)
            closeHand(contServo)
            sigVal = reset(contServo)

#----- Thread 0 Code -----#
