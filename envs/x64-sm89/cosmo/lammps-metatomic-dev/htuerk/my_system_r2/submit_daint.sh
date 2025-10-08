#!/bin/bash -l
#SBATCH --job-name=lammps-cosmo
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --gpus-per-task=1
#SBATCH --account=lp117
#SBATCH --partition=normal
#SBATCH --uenv=lammps-metatomic/rc2
#SBATCH --view=lammps

export MPICH_GPU_SUPPORT_ENABLED=1

ulimit -s unlimited

srun lmp -in system.in -k on g 1 -sf kk -pk kokkos gpu/aware on
