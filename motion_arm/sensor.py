from machine import Pin, ADC, PWM
from time import sleep

button = Pin(1, Pin.IN, Pin.PULL_UP)
touch = ADC(Pin(28))
touch_value = touch.read_u16()
touch_list = []

def calibrate(data):
    print("press button to begin calibration")
    while data == []:    
        if button.value() == 0:
            print("do not press sensor")
            sleep(1)
            for i in range(50):
                for i in range(20):
                    touch_value = touch.read_u16()    
                data.append(touch_value)
                sleep(0.05)                    
            print("calibration complete")

def search(sensor):
    touch_value = sensor.read_u16()
    sleep(0.5)
    return dev * 7.0 + avg
