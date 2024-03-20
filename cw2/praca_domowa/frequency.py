import matplotlib.pyplot as plt
import numpy as np


MIN_FREQ = 30
MAX_FREQ = 1000
DURATION = 0.05


def generate_pwm_signal(min_frequency, max_frequency, duration):
    t = np.linspace(0, duration, int(45000 * duration / 2), endpoint=False)
    freqencies = np.linspace(min_frequency, max_frequency, len(t))
    pwm_signal = np.zeros_like(t)

    for i, f in enumerate(freqencies):
        pwm_signal[i] = np.sin(2 * np.pi * f * t[i]) > 0

    t = np.concatenate((t, t + duration / 2))
    pwm_signal = np.concatenate((pwm_signal, pwm_signal[::-1]))

    return t, pwm_signal


def main():

    t, pwm_signal = generate_pwm_signal(MIN_FREQ, MAX_FREQ, DURATION)

    plt.plot(t, pwm_signal)
    plt.title("PWM Signal with Increasing and Decreasing Frequency")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    plt.savefig("variable_frequency.png")


if __name__ == "__main__":
    main()
