import numpy as np
import ase.io
from ase.calculators.espresso import Espresso
import os

folders=np.array(["4caco3-Eslam-1","4caco3-Eslam-2","8caco3-Eslam-1","8caco3-Eslam-2"])
#folders=np.array(["4caco3","caco3-2cv"])
os.system("./get_max_numbers.sh > tmp")
max_numbers=np.genfromtxt("tmp").astype("int")

for folder, max_number in zip(folders,max_numbers):
    #################################
    # Coordinates
    #################################
    file_coord = open(folder + "/extracted-confs/coord.raw", "w")
    file_energy = open(folder + "/extracted-confs/energy.raw", "w")
    file_force = open(folder + "/extracted-confs/force.raw", "w")
    #file_virial = open(folder + "/extracted-confs/virial.raw", "w")
    file_box = open(folder + "/extracted-confs/box.raw", "w")
    file_type = open(folder + "/extracted-confs/type.raw", "w")
    types_written=False
    for i in range(max_number+1):
        try:
            conf=ase.io.read(folder + "/extracted-confs/pw-caco3-" + str(i) + ".out",format='espresso-out')
        except:
            print("Configuration " + str(i) + " could not be read")
        else:
            try:
                conf.get_forces()
            except:
                print("Forces missing from file" + str(i))
            else:
                file_coord.write(' '.join(conf.get_positions().flatten().astype('str').tolist()) + '\n')
                file_energy.write(str(conf.get_potential_energy()) + '\n')
                file_force.write(' '.join(conf.get_forces().flatten().astype('str').tolist()) + '\n')
                #file_virial.write(' '.join(conf.get_stress(voigt=False).flatten().astype('str').tolist()) + '\n')
                file_box.write(' '.join(conf.get_cell().flatten().astype('str').tolist()) + '\n')
                if (not(types_written)):
                    types = np.array(conf.get_chemical_symbols())
                    types[types=="Ca"]="0"
                    types[types=="C"]="1"
                    types[types=="O"]="2"
                    types[types=="H"]="3"
                    file_type.write(' '.join(types.tolist()) + '\n')
                    types_written=True
    file_coord.close()
    file_energy.close()
    file_force.close()
    #file_virial.close()
    file_box.close()
    file_type.close()

