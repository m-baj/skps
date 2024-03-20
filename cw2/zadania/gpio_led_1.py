import gpio4
import time

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' 

for i in range(10):
    gpio27.value = 0
    time.sleep(0.5)
    gpio27.value = 1
    time.sleep(0.5)

gpio27.export = False # release the pin