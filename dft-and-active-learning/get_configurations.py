import numpy as np
import ase.io
from ase.calculators.espresso import Espresso
import os

################################
# QE options
################################

pseudopotentials = {'Ca': 'Ca_ONCV_PBE_sr.upf',
                    'C': 'C_ONCV_PBE_sr.upf',
                    'O': 'O_ONCV_PBE_sr.upf',
                    'H': 'H_ONCV_PBE_sr.upf'}

input_qe = {
            'calculation':'scf',
            'outdir':'./',
            #'pseudo_dir':'/home/ppiaggi/pseudos',
            'pseudo_dir':'/global/homes/p/ppiaggi/QuantumEspresso/pseudos',
            'disk_io':'none',
            'system':{
              'ecutwfc': 110,
              'input_dft': 'SCAN',
             },
            'electrons':{
               'mixing_beta': 0.5,
               'electron_maxstep':1000,
             },
}

#################################
# Load error file
#################################

error_threshold=0.4
error_threshold_max=10
max_num_configurations=200
step=1

#################################
# Load trajectory
#################################

folders=np.array(["caco3-2cv-430K"])

for folder in folders:
   print("Folder " + folder)
   counter1=0 # Number of configurations written
   os.system('mkdir ' + folder + '/extracted-confs')
   traj=ase.io.read(folder + '/dump.water',format='lammps-dump-text',index=':')
   errors=np.genfromtxt(folder + "/md.out")
   counter2=0 # Frame number
   for conf in traj:
      if (counter2==0): # Skip first frame (avoid recalculating)
              counter2 += 1
              continue
      if ((counter2%step)==0):
         if (errors[counter2,4]>error_threshold and errors[counter2,4]<error_threshold_max):
            new_species=np.array(conf.get_chemical_symbols())
            new_species[new_species=='H']='Ca'
            new_species[new_species=='He']='C'
            new_species[new_species=='Li']='O'
            new_species[new_species=='Be']='H'
            conf.set_chemical_symbols(new_species)
            ase.io.write(folder + '/extracted-confs/pw-caco3-' + str(counter1) + '.in',conf, format='espresso-in',input_data=input_qe, pseudopotentials=pseudopotentials, tprnfor=True)
            counter1 += 1
            print("Extracting from folder ",folder," configuration ", counter2, " - total configurations extracted ",counter1, " . Max error from this configuration is ",errors[counter2,4], " . Num atoms is ",new_species.shape[0])
      if (counter1>max_num_configurations):
         break
      counter2 += 1
