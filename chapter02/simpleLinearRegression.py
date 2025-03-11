import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

if __name__ == "__main__":
    np.random.seed(12345)
    x = np.linspace(0, 10, 1000)

    # y = 2.5x + 5 + (noise term)
    y_true = 2.5*x + 5.0 + np.random.normal(0, 2.5, size=len(x))

    slope, intercept, r_value, p_value, std_err = linregress(x, y_true)
    y_pred = slope * x + intercept

    plt.scatter(x, y_true, label="Data", color="blue")
    plt.plot(x, y_pred, label=f"$y = {slope:.2f}x + {intercept:.2f}$", color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Linear Regression")
    plt.legend()
    plt.show()
    sys.exit(0)

