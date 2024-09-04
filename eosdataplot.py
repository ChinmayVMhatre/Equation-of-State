import numpy as np
import ase
from ase import Atoms
from ase.io.trajectory import Trajectory
from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt

numbers =[0,1,2,3,4,5]

u_p = []
u_v = []
U_p = []
U_v = []
u_P = []
u_V = []
U_P = []
U_V = []

for i in numbers:
  u = ase.io.read(f"./PBED3/{i}/POSCAR",format = 'vasp')
  u_o = ase.io.read(f"./PBED3/{i}/OUTCAR",format = 'vasp-out')
  u_p.append(u_o.get_potential_energy())
  u_v.append(u_o.get_volume())

for i in numbers:
  u = ase.io.read(f"./ogPBE/{i}/POSCAR",format = 'vasp')
  u_o = ase.io.read(f"./ogPBE/{i}/OUTCAR",format = 'vasp-out')
  u_P.append(u_o.get_potential_energy())
  u_V.append(u_o.get_volume())


eos_vdw = EquationOfState(u_v, u_p, eos='birchmurnaghan')

eos_pbe = EquationOfState(u_V, u_P, eos='birchmurnaghan')

v0_pbe, e0_pbe, B_pbe = eos_pbe.fit()

v0_vdw, e0_vdw, B_vdw = eos_vdw.fit()


data_vasp = eos_pbe.getplotdata()

DATA_vasp = eos_vdw.getplotdata()

eos_pbe.plot()

eos_vdw.plot()


print(f'volume for PBE-D3:{v0_vdw} A^3')

print(f'volume for PBE:{v0_pbe} A^3')

volume_array=np.array([v0_vdw,v0_pbe])
print(type(volume_array))

ang = np.sin(1.0471975511965976)
lc = (4*volume_array/ang)**(1/3)

print(lc)

