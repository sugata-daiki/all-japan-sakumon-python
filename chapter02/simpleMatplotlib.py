import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_arr = np.arange(0.0, 1.0, 0.01, dtype=float)

    plt.plot(x_arr, x_arr, label="$y = x$")
    plt.plot(x_arr, x_arr**2, label="$y = x^2$")
    plt.plot(x_arr, - x_arr**3 + x_arr, label="$y = - x^3 + x$")
    plt.plot(x_arr, np.sin(x_arr), label="$y=\sin x$")

    plt.title("simple mathematical functions")
    plt.legend(loc="upper right")
    plt.show()
    sys.exit(0)
