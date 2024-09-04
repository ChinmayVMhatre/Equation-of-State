import numpy as np
import ase
from ase import Atoms
from ase.io.trajectory import Trajectory
#from deepmd.calculator import DP
from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt

numbers =[0,1,2,3,4,5]

#numbers =[13,14,15,16,17,18,19,20,21,22,23,24,25]

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

#for i in numbers:
#  u = ase.io.read(f"./PBEsol/{i}/POSCAR",format = 'vasp')
#  u_o = ase.io.read(f"./PBEsol/{i}/OUTCAR",format = 'vasp-out')
#  U_p.append(u_o.get_potential_energy())
#  U_v.append(u_o.get_volume())

for i in numbers:
  u = ase.io.read(f"./ogPBE/{i}/POSCAR",format = 'vasp')
  u_o = ase.io.read(f"./ogPBE/{i}/OUTCAR",format = 'vasp-out')
  u_P.append(u_o.get_potential_energy())
  u_V.append(u_o.get_volume())

#for i in numbers:
#  u = ase.io.read(f"./vdw-DF/{i}/POSCAR",format = 'vasp')
#  u_o = ase.io.read(f"./vdw-DF/{i}/OUTCAR",format = 'vasp-out')
#  U_P.append(u_o.get_potential_energy())
#  U_V.append(u_o.get_volume())


eos_vdw = EquationOfState(u_v, u_p, eos='birchmurnaghan')
#eos_sol = EquationOfState(U_v, U_p, eos='birchmurnaghan')
eos_pbe = EquationOfState(u_V, u_P, eos='birchmurnaghan')
#eos_vdw_df = EquationOfState(U_V, U_P, eos='birchmurnaghan')

#print(u_v)

v0_pbe, e0_pbe, B_pbe = eos_pbe.fit()
#v0_sol, e0_sol, B_sol = eos_sol.fit()
v0_vdw, e0_vdw, B_vdw = eos_vdw.fit()
#v0_v,e0_v,B_v = eos_vdw_df.fit()

data_vasp = eos_pbe.getplotdata()
#data_VASP = eos_sol.getplotdata()
DATA_vasp = eos_vdw.getplotdata()
#d_vasp = eos_vdw_df.getplotdata()

eos_pbe.plot()
#eos_sol.plot()
eos_vdw.plot()
#eos_vdw_df.plot()

#print(u_v)

#plt.figure(1)
#plt.plot(u_v, u_p,'ro-',label=fr'PBED3')
#plt.plot(U_v, U_p,'bo-',label=fr'PBEsol')
#plt.plot(u_V, u_P,'go-',label=fr'PBE')
##plt.plot(U_V, U_P,'go-',label=fr'vdw-DF')
#plt.legend(frameon = True)
#plt.xlabel(r'Volume ($ \AA^3 $)')
#plt.ylabel('Energy (eV)')
#plt.tick_params(direction = 'in', right = True, top = True)#, labeltop = True, labelright = True)
#plt.savefig("eosplot.png",dpi=600)

#plt.figure(2)
#plt.plot(U_v, U_p,'bo-',label=fr'PBEsol')
#plt.legend(frameon = True)
#plt.xlabel(r'Volume ($ \AA^3 $)')
#plt.ylabel('Energy (eV)')
#plt.tick_params(direction = 'in', right = True, top = True)#, labeltop = True, labelright = True)
#plt.savefig("eosplot1.png",dpi=600)

#plt.figure(3)
#plt.plot(u_V, u_P,'go-',label=fr'PBE-D3')
#plt.legend(frameon = True)
#plt.xlabel(r'Volume ($ \AA^3 $)')
#plt.ylabel('Energy (eV)')
#plt.tick_params(direction = 'in', right = True, top = True)#, labeltop = True, labelright = True)
#plt.savefig("eosplot2.png",dpi=600)

#plt.figure(2)
#plt.plot(U_V, U_P,'yo-',label=fr'vdw-DF')
#plt.legend(frameon = True)
#plt.xlabel(r'Volume ($ \AA^3 $)')
#plt.ylabel('Energy (eV)')
#plt.tick_params(direction = 'in', right = True, top = True)#, labeltop = True, labelright = True)
#plt.savefig("eosplot1.png",dpi=600)


print(f'volume for PBE-D3:{v0_vdw} A^3')
#print(f'volume for PBEsol:{v0_sol} A^3')
print(f'volume for PBE:{v0_pbe} A^3')
#print(f'volume for vdw-DF:{v0_v} A^3')

#volume_array=np.array([v0_vdw,v0_sol,v0_pbe,v0_v])
volume_array=np.array([v0_vdw,v0_pbe])
print(type(volume_array))

ang = np.sin(1.0471975511965976)
lc = (4*volume_array/ang)**(1/3)

print(lc)

