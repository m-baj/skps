import gpio4
import time
sensor = gpio4.SysfsGPIO(19)
sensor.export = True
sensor.direction = 'in'
trigger = gpio4.SysfsGPIO(27)
trigger.export = True
trigger.direction = 'out'

trigger.value = 0
time.sleep(0.00001)
trigger.value = 1
time.sleep(0.00001)

value = 0
t = time.time()
while True:
    print(sensor.value)
    # if(value != sensor.value):
    #     d = time.time() - t
    #     t = time.time()
    #     print(d * 34300 / 2)
    #     value = sensor.value

sensor.export = False