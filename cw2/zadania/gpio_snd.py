import gpio4, time
from math import sin, pi
 
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 987.77, 1046.50]
one_duration = 1
fill = 0.5

buzzer = gpio4.SysfsGPIO(19)
buzzer.export = True
buzzer.direction = 'out'


def calculate_up_down(frequency: int, fill: float = 0.5):
    t = 1 / frequency
    hi = t * fill
    lo = t - hi

    return hi, lo


def cycle(gpio: gpio4.SysfsGPIO, frequency: int, fill: float = 0.5):
    hi, lo = calculate_up_down(frequency, fill)
    gpio.value = 1
    time.sleep(hi)
    gpio.value = 0
    time.sleep(lo)



for frequency in frequencies:
    cycle(buzzer, frequency, fill)
    time.sleep(0.1)

buzzer.export = False