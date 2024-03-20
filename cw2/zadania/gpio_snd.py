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
    up = t * fill
    down = t - up

    return up, down


def cycle(gpio: gpio4.SysfsGPIO, frequency: int, fill: float = 0.5):
    up, down = calculate_up_down(frequency, fill)
    gpio.value = 1
    time.sleep(up)
    gpio.value = 0
    time.sleep(down)



for f in frequencies:
    timestamp = time.time() + one_duration
    while time.time() < timestamp:
        cycle(buzzer, f, fill)

buzzer.export = False