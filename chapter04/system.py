import torch
import numpy as np

class System:
    def __init__(self, natoms, nreplicas, precision, device):
        self.pos = torch.zeros(nreplicas, natoms, 3)
        self.forces = torch.zeros(nreplicas, natoms, 3)

        self.device = device
        self.to_(device)
        self.precision_(precision)

    def initialize_pos(self, pos):
        self.pos = pos

    @property
    def natoms(self):
        return self.pos.shape[0]

    def to_(self, device):
        self.forces = self.forces.to(device)
        self.pos = self.pos.to(device)

    def precision_(self, precision):
        self.forces = self.forces.type(precision)
        self.pos = self.pos.type(precision)

    
