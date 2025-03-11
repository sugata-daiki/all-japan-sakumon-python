import sys
import numpy as np
import matplotlib.pyplot as plt

"""
Implementation retrieved from https://labo-code.com/python/elliptic_equation/
"""

def _set_initial_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
) -> None:

    for j in range(1, grid_counts_y):
        for i in range(1, grid_counts_x):
            array_2d[i][j] = 0.0001


def _set_boundary_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
    grid_space: float,
) -> None:

    for i in range(grid_counts_x + 1):
        array_2d[i][0] = 0.0

    for i in range(grid_counts_x + 1):
        array_2d[i][grid_counts_y] = (
            4 * (grid_space * i) * (1.0 - grid_space * i)
        )


def _is_converged(*, U: list, UF: list, M: int, N: int) -> bool:
    ERROR_CONSTANT: float = 0.0001
    sum: float = 0.0
    sum0: float = 0.0

    for j in range(1, N):
        for i in range(1, M):
            sum0 += abs(U[i][j])
            sum += abs(U[i][j] - UF[i][j])

    sum = sum / sum0
    return sum <= ERROR_CONSTANT


def calculate_equation(*, M: int, N: int, H: float, MK: int) -> (list, int):
    U: list = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]
    UF: list = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]

    _set_initial_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_counts_y=N,
    )
    _set_boundary_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_counts_y=N,
        grid_space=H,
    )

    calc_count: int = 0
    for _ in range(MK):
        for j in range(1, N):
            for i in range(1, M):
                UF[i][j] = U[i][j]
                U[i][j] = (
                    U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1]
                ) / 4.0
        calc_count += 1

        if _is_converged(U=U, UF=UF, M=M, N=N):
            print("Converged.")
            break
    return U, calc_count


def color_plot(
        *, 
        array_2d: list, 
        grid_counts: int, 
        grid_space: float,
    ) -> None:

    min_x_y = 0.0 - grid_space / 2
    max_x_y = grid_space * grid_counts + grid_space / 2
    extent=(min_x_y, max_x_y, min_x_y, max_x_y)
    
    array_2d = np.array(array_2d).T
    plt.imshow(
        array_2d,
        cmap="viridis",
        interpolation="none",
        aspect="auto",
        origin="lower",
        extent=extent,
    )
    plt.colorbar()
    plt.savefig("./2d_color_plot.png", format="png")


def output_result_file(
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
    grid_space: float,
    calc_count: int,
) -> None:
    with open("./calculated_result.txt", "w") as file:
        file.write(f"# This file shows calculated result as below.\n\n")
        file.write(f"# Calculation Parameters.\n")
        file.write(f"grid_counts_x: {grid_counts_x}\n")
        file.write(f"grid_counts_y: {grid_counts_y}\n")
        file.write(f"grid_space: {grid_space}\n")
        file.write(f"calculation_count: {calc_count}\n\n")

        file.write(f"# Calculated Matrix H.\n")
        for row in array_2d:
            line = " ".join(map(str, row))
            file.write(line + "\n")


if __name__ == "__main__":
    grid_counts_x: int = 10
    grid_counts_y: int = 10
    grid_space: float = 0.1
    total_calc_count: int = 1000

    array_2d, calc_count = calculate_equation(
        M=grid_counts_x,
        N=grid_counts_y,
        H=grid_space,
        MK=total_calc_count,
    )
    color_plot(
        array_2d=array_2d,
        grid_counts=grid_counts_x,
        grid_space=grid_space,
    )
    output_result_file(
        array_2d=array_2d,
        grid_counts_x=grid_counts_x,
        grid_counts_y=grid_counts_y,
        grid_space=grid_space,
        calc_count=calc_count,
    )
    sys.exit(0)
