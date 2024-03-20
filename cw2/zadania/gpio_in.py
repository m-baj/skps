import gpio4

sw1 = gpio4.SysfsGPIO(18)
sw1.export = True
sw1.direction = 'in'
diode = gpio4.SysfsGPIO(27)
diode.export = True
diode.direction = 'out'

while True:
    if sw1.value ==0:
        diode.value = 1
    else:
        diode.value = 0

sw1.export = False
diode.export = False
