import numpy as np
import matplotlib.pyplot as plt


MIN_PERCENT = 10
MAX_PERCENT = 90


def generate_variable_fill_pwm(frequency, fill):
    period = 1 / (frequency * 10000)
    t = np.arange(0, 1, period)
    pwm_signal = np.zeros(len(t))
    pwm_signal[: int(fill * len(t))] = 1
    return t, pwm_signal


def main():
    t_full, pwm_full = [], []
    for index, fill in enumerate(range(MIN_PERCENT, MAX_PERCENT, 5)):
        t, pwm_signal = generate_variable_fill_pwm(1, fill / 100)
        t += index
        t_full = np.concatenate((t_full, t))
        pwm_full = np.concatenate((pwm_full, pwm_signal))

    t_full = np.concatenate((t_full, t_full + 16))
    pwm_full = np.concatenate((pwm_full, pwm_full[::-1]))

    plt.figure(figsize=(8, 4))
    plt.plot(t_full, pwm_full)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("PWM Signal with Increasing Fill")
    plt.grid(True)
    plt.savefig("variable_fill.png")
    plt.show()


if __name__ == "__main__":
    main()
