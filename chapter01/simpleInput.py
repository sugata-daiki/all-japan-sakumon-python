import sys
import numpy as np

if __name__ == '__main__':
    arr = np.loadtxt("test.txt", dtype=int)
    print(arr)
    sys.exit(0)
