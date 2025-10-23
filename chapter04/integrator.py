import numpy as np
import torch
import system

BOLTZMANN = 0.001987191


def langevin(pos, coeff, dt, device):
    csi = torch.randn_like(pos, device=device) * coeff
    pos += csi*dt

class Integrator():
    def __init__(self, system, timestep, diffconst, T):
        self.dt = timestep
        self.system = system
        self.energy_unit = BOLTZMANN*T
        self.coeff = torch.sqrt(2.0*diffconst).to(self.system.device)

    def add_langevin_fluctuation(self):
        langevin(self.system.pos, self.coeff, self.dt, self.system.device)


