#!/bin/bash
#SBATCH --qos=regular
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=2
#SBATCH -C cpu
#SBATCH -t 00:50:00
#SBATCH -J caco3

export SLURM_CPU_BIND="cores"
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
export OMP_NUM_THREADS=2
export HDF5_USE_FILE_LOCKING=FALSE

module load PrgEnv-intel
PW=/global/homes/p/ppiaggi/Programs/Perlmutter/QuantumEspresso/q-e-qe-6.4.1/bin/pw.x
srun $PW -input REPLACE1 > REPLACE2
