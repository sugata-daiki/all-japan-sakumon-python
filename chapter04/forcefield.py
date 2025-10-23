import torch
import system
import integrator

class ForceField():
    def __init__(self, integrator):
        self.integrator = integrator
        ### HarmonicForceField constants
        self.spring = 0.0
        self.bondLength = 0.0

    def set_const(self, spring, bondLength):
        self.spring = spring
        self.bondLength = bondLength

    def HarmonicForceField(self, rel_pos):
        norm = torch.norm(rel_pos)
        V_b = 0.5*self.spring*(norm - self.bondLength)**2
        return V_b
    def add_HarmonicForceField(self, posi, posj, pot, rel_pos):
        pot.backward()
        F = - rel_pos.grad
        langevin_scaled_F = F*self.integrator.dt/self.integrator.energy_unit

        posi += langevin_scaled_F
        posj -= langevin_scaled_F

        rel_pos.grad.zero_()


