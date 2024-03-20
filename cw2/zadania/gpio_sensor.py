import gpio4
import time
sensor = gpio4.SysfsGPIO(19)
sensor.export = True
sensor.direction = 'in'
trigger = gpio4.SysfsGPIO(27)
trigger.export = True
trigger.direction = 'out'

def measure(sensor, trigger):
    trigger.value = 0
    time.sleep(0.00001)
    trigger.value = 1
    time.sleep(0.00001)
    trigger.value = 0

    while sensor.value == 0:
        pass

    t = time.time()

    while sensor.value == 1:
        pass

    return (time.time() - t) * 34300 / 2


while True:
   res = measure(sensor, trigger)
   print(res)

sensor.export = False