import gpio4


frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 987.77, 1046.50]

def play_tone(pin, frequency, duration):
    pwm = gpio4.PWM(pin)
    pwm.export = True
    pwm.period = int(1 / frequency * 1e9)
    pwm.duty_cycle = int(pwm.period / 2)
    pwm.enable = True
    time.sleep(duration)
    pwm.export = False


def main():
    pin = 12
    for frequency in frequencies:
        play_tone(pin, frequency, 0.5)
    pwm.export = False

if __name__ == '__main__':
    main()