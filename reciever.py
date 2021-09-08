from microbit import *
import radio

'''
Reciever, using batteries. 
To conserver energy, lower display brightness and 
only check for new messages every 20 minutes. 
'''    

radio.config(group=1)
msg = ""

while True:
    radio.on()
    sleep(1000)

    message = radio.receive()

    if message:
        msg = message
        if msg == '0':
            msg = ''
            display.clear()
        display.show(msg)
        for i in range(5):
            for j in range(5):
                 if display.get_pixel(i, j):
                     display.set_pixel(i, j, 7)
        

    radio.off()
    sleep(1200000)