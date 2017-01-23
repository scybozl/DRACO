#!/bin/bash -l
# Standard output and error:
#SBATCH -o ./tjob.out.%j
#SBATCH -e ./tjob.err.%j
# Initial working directory:
#SBATCH -D ./
# Job Name:
#SBATCH -J Sherpa
# Queue (Partition):
#SBATCH --partition=general
# Number of nodes and MPI tasks per node:
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=32
#
#SBATCH --mail-type=none
#SBATCH --mail-user=<userid>@rzg.mpg.de
#
# Wall clock limit:
#SBATCH --time=24:00:00

# Run the program:

cd /ptmp/lscyboz/SHERPA-MC-2.2.0/emubB
srun ../bin/Sherpa -f Run_emubB.dat > prog.out
