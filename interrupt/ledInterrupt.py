
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
signal = Pin(2, Pin.IN, Pin.PULL_DOWN)
blue = Pin(3, Pin.OUT)
yellow = Pin(4, Pin.OUT)
interrupt_flag = 0

def callback(signal):
    global interrupt_flag
    interrupt_flag = 1
    
def blink(pin):
        pin.high()
        time.sleep(1)
        pin.low()
        time.sleep(1)
    
signal.irq(trigger=Pin.IRQ_RISING,handler = callback)
#blue.high()
#yellow.low()
while True:
    blink(blue)
    #blue.high()
    #yellow.low()
    if interrupt_flag is 1:
        blue.low()
        interrupt_flag = 0
        led.toggle()
        blink(yellow)
