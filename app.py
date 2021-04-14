import time
from DMXEnttecPro import Controller
dmx = Controller('/dev/cu.usbserial-EN246934')

 
for ch in range(1,8):
    dmx.set_channel(ch, 255)

dmx.submit()

for val in range(255):
    dmx.set_channel(1, val)  
    dmx.submit()
    # print("sending ", val)
    time.sleep(0.01)


for val in range(255,0, -1):
    dmx.set_channel(1, val) 
    dmx.submit()
    # print("sending ", val)
    time.sleep(0.01)

