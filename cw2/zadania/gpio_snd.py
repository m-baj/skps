import gpio4



import gpio4, time
from math import sin, pi
 
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 987.77, 1046.50]
one_duration = 1
fill = 0.5

buzzer = gpio4.SysfsGPIO(19)
buzzer.export = True
buzzer.direction = 'out'

while True:
    buzzer.value = 1
    time.sleep(1)
    buzzer.value = 0

time.sleep(10)

# try:
#     for frequency in frequencies:
#         period = 1 / frequency
#         t = time.time()
#         while time.time() - t < one_duration:
#             if time.time() - t < fill * period:
#                 buzzer.value = 1
#             else:
#                 buzzer.value = 0
# except:
#     raise Exception
# finally:
buzzer.export = False


