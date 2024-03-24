from gpiozero import Button, LED
from time import sleep
output = LED(22)
button = Button(18)
previous_state = 0
current_state = 1

while True:
    if button.is_pressed:
        if previous_state != current_state:
            print("signal sent")
            output.on()
            current_state = 0
            sleep(0.5)
    else:
        output.off()
        current_state = 1
        print("Signal Not Sent")
        sleep(0.5)
        
