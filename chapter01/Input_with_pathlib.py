import numpy as np
import sys
from pathlib import Path

args = sys.argv

def make_filePath(file_name: str) -> str:
    """Make file path.

    Args:
        file_name (str): name of input file

    Returns:
        str: path to input file
        
    """
    exe_dir = Path(__file__).parent
    file_path = exe_dir / file_name

    if file_path.exists():
        return file_path
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

def main() -> int:
    args = sys.argv

    file_name = args[1]
    file_path = make_filePath(file_name)

    with open(file_path) as f:
        tmp = f.read().splitlines()

    input_arr = np.array([np.array(tmp[i].split(), dtype=int) for i in range(len(tmp))], dtype=object)

    print(input_arr)

    return 0

if __name__ == '__main__':
    sys.exit(main())
