import numpy as np
import torch
from system import System
from integrator import Integrator
from forcefield import ForceField

def main():

    ### parameters
    natoms = 100
    nreplicas = 1
    nsteps = 10000
    timestep = 0.001
    temperature = 300
    precision = torch.float32
    device = 'cpu'
    diffusionConst = torch.tensor(10.0)
    spring = 2.5
    bondLength = 10.0


    ### system/integrator/forcefield setup
    system = System(natoms, nreplicas, precision, device)
    integrator = Integrator(system, timestep, diffusionConst, temperature)
    ff = ForceField(integrator)

    pos = torch.zeros(nreplicas, natoms, 3)
    pos[0, :, 0] = torch.arange(0, natoms, 1)*bondLength
    system.initialize_pos(pos)

    ff.set_const(spring, bondLength)

    ### simulation
    for _ in range(nsteps):
        integrator.add_langevin_fluctuation()
        Harmonic_rel_pos = (system.pos[:, :(natoms-1), :] - system.pos[:, 1:natoms, :]).clone().detach().requires_grad_(True)
        pot = ff.HarmonicForceField(Harmonic_rel_pos)
        print(f"energy : {torch.sum(pot)} kcal/mol")

        ff.add_HarmonicForceField(system.pos[:, :(natoms-1), :], system.pos[:, 1:natoms, :], pot, Harmonic_rel_pos)


if __name__ == "__main__":
    main()
