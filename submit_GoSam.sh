#!/bin/bash -l
# Standard output and error:
#SBATCH -o ./tjob.out.%j
#SBATCH -e ./tjob.err.%j
# Initial working directory:
#SBATCH -D ./
# Job Name:
#SBATCH -J test_slurm
# Queue (Partition):
#SBATCH --partition=general
# Number of nodes and MPI tasks per node:
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=16
#
#SBATCH --mail-type=none
#SBATCH --mail-user=<userid>@rzg.mpg.de
#
# Wall clock limit:
#SBATCH --time=24:00:00

# Run the program:

module load gcc/6.2
export PATH=/home/iwsatlas1/scyboz/Work/HERWIG/bin:$PATH
cd 

make -j 8
