import gpio4

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' 

for i in range(10):
    gpio27.value = True
    gpio27.value = False

gpio27.export = False # release the pin