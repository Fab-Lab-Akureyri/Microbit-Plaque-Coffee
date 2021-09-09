from microbit import *
import radio
import utime

'''
Sender for coffee counter. 
Connected through USB on desk so not attempts to save batteries. 
'''

radio.config(group=1, power=1)

count = 0

def show():
    if count > 0:
        display.show(str(count))
    else: 
        display.clear()

radio.on()

while True:
    if button_a.was_pressed():
        count += 1

    if button_b.was_pressed():
        count = 0

    radio.send(str(count))

    show()