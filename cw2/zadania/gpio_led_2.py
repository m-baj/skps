
import gpio4
import time

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' 

MIN_PERCENT = 0
MAX_PERCENT = 100


def generate_variable_fill_pwm(frequency, fill):
    period = 1 / (frequency * 10000)
    len_t = int(1/period)
    pwm_signal = [0] * len_t
    pwm_signal[: int(fill * len_t)] = 1
    return pwm_signal


def main():
    for index, fill in enumerate(range(MIN_PERCENT, MAX_PERCENT, 10)):
        pwm_signal = generate_variable_fill_pwm(1, fill / 100)
        t = 1/len(pwm_signal)
        for value in pwm_signal:
            gpio27.value = value
            time.sleep(t)

gpio27.export = False # release the pin