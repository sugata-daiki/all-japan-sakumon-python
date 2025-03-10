import sys
import numpy as np

if __name__ == '__main__':

    fibonacci_seq = [1, 1]
    [fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2]) for _ in range(8)]
    output_arr = np.array([[i+1, fibonacci_seq[i]] for i in range(10)], dtype=int)

    np.savetxt("test.txt", output_arr, fmt='%s')
    """
    with open("test.txt", "w") as f:
        f.writelines(" ".join(map(str, row)) + "\n" for row in output_arr)
    """
    sys.exit(0)

