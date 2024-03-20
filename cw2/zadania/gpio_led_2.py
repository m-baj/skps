import gpio4, time
from math import sin, pi
 
led27 = gpio4.SysfsGPIO(27)
led27.export = True
led27.direction = 'out'

timestamp = 0
freq = 100
wait = 1e-4

try:
    while timestamp < 10:
        duty_cycle = abs(sin(pi*timestamp/2))
        if timestamp % (1 / freq) < (1/freq)*duty_cycle:
            led27.value = 1
        else:
            led27.value = 0
        timestamp += wait
        time.sleep(wait)
except:
    raise Exception
finally:
    led27.export = False