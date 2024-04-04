#temporary test file

from arm_movements import *
from hand import *
import _thread as thread

#----- Thread 1 Code -----#

thread1 = True

servo1 = PWM(Pin(3))
servo2 = PWM(Pin(4))

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
