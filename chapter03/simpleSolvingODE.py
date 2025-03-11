import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(x: float, t: float) -> float:
    return -x

if __name__ == "__main__":
    t = np.linspace(0.0, 10.0, 100)
    x0 = 1.0
    
    x = odeint(f, x0, t)

    plt.plot(t, x)
    plt.show()
    sys.exit(0)

    
