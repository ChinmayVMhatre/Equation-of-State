#step 1 : Import POSCAR to your current folder, which will be read by the script
#step 2 : Change the numpy array in line 15, this is the range of volume change you wanted. This case, it is -5% to 10% of original volume.
#step 3 : You will get series of POSCARs. You can monitor the volume change with "  ase gui POSCAR* " command. 


import subprocess
import numpy as np
import ase
from ase import Atoms
from ase.io.trajectory import Trajectory

u = ase.io.read("POSCAR",format='vasp')
cell = u.get_cell()
i = 0

for x in np.linspace(0.95,1.1,11):
  u.set_cell(cell * x, scale_atoms=True)
  np.savetxt(f'POSCAR{i}',u.get_positions()[0])
  ase.io.write(f'POSCAR{i}',u,format='vasp')
  i+=1

