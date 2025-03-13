import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# system parameters
L = 1.0
Nx = 100
dx = L / Nx
dt = 0.0005
T = 1.0
Nt = int(T / dt)
D = 0.1

# stability condition 
alpha = D * dt / dx**2
assert alpha <= 0.5, f"[ warning ] unstable condition: alpha={alpha} > 0.5"

# initialization 
U = np.zeros(Nx)
U.fill(300) # 300K at 1/2 <= x < 1.0
U[:Nx//2] = 280 # 280K at x < 1/2 
U[0] = 280
U[-1] = 300 

# centered difference method 
main_diag = (1 - 2 * alpha) * np.ones(Nx)
off_diag = alpha * np.ones(Nx - 1)
A = sp.diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')

# boundary condition : 300K at x = 1.0, 280K at x = 0.0 (identical to an initial value)
A = A.toarray()
A[0, :] = 0
A[0, 0] = 1
A[-1, :] = 0
A[-1, -1] = 1
A = sp.csr_matrix(A)

# animation setup
fig, ax = plt.subplots()
x = np.linspace(0, L, Nx)
line, = ax.plot(x, U, lw=2)
ax.set_ylim(270, 310)
ax.set_xlabel("x")
ax.set_ylabel("Temperature (K)")
ax.set_title("1D Heat Diffusion Equation")

def update(frame):
    global U
    U = A @ U
    line.set_ydata(U)
    return line,

ani = animation.FuncAnimation(fig, update, frames=Nt, interval=30, blit=True)
plt.show()
