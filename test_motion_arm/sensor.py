from machine import Pin, ADC, PWM
from time import sleep, sleep_ms
from statistics import stdev, mean

touch = ADC(Pin(28))
data = []
sigVal = 0

# gathers baseline data into one list
def calibrate():   
    data = []   
    print("do not press sensor")
        
    # collecting baseline data
    for i in range(50):
        touch_value = touch.read_u16()
        data.append(touch_value)
        sleep(0.1)
        
    print("calibration complete")
        
    sigVal = stdev(data) * 7.0 + mean(data)
    return sigVal

# gathers sensor data and returns when the value is signifigant
def search(touch, sigVal):
    touch_value = touch.read_u16()
    sleep(0.5)
    if touch_value > sigVal:
        return True