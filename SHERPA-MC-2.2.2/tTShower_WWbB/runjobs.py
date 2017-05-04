from subprocess import Popen, PIPE #, check_output
from os import chdir, getcwd
from mpmath import *
from sys import argv, exit
mp.dps = 10

part = argv[1] # LO, BVI, RS, BVIRS
TMASS = float(argv[2])
scalefac = float(argv[3])
mode = argv[4] # grid or event
submit = 'slurm' # choose ['serial','slurm','condor']
nstart = 1 # first job number
n = 5 # number of jobs
mpithreads = 8

if mode == "grid":
    err = 0.01
elif mode == "event":
    err = 0.1

Gmu = 1.16637*10**(-5)
mw = 80.385
alphas = {165.0: {0.5: 0.1198091780, 1.0: 0.1083299807, 2.0: 0.0988931625}, 
          172.5: {0.5: 0.1189991917, 1.0: 0.1076702244, 2.0: 0.0983446040}, 
          180.0: {0.5: 0.1182342964, 1.0: 0.1070463406, 2.0: 0.0978254289}}

def gammaW( part , mt , scale ):
    gammaW0 = (2*3 + 3)*Gmu*mw**3/(6*sqrt(2)*pi)
    if part == "LO":
        return gammaW0
    elif part == "RS" or part == "BVI" or part == "BVIRS":
        gammaW1 = gammaW0*alphas[mt][scale]/pi
        return gammaW0 + gammaW1

def gammaT( part , mt , scale ):
    y = (mw/mt)**2
    if part == "LO":
        return ((Gmu*mt**5)/(16*sqrt(2)*pi**2*mw**2))*pi*y*(2*(1 - y)**2*(1 + 2*y))
    elif part == "RS" or part == "BVI" or part == "BVIRS":
        return ((Gmu*mt**5)/(16*sqrt(2)*pi**2*mw**2))*pi*y*(2*(1 - y)**2*(1 + 2*y) - ((2*alphas[mt][scale])/(3*pi))*(2*(1 - y)**2*(1 + 2*y)*(pi**2 + 2*polylog(2, y) - 2*polylog(2, 1 - y)) + 4*y*(1 - y - 2*y**2)*log(y) + 2*(1 - y)**2*(5 + 4*y)*log(1 - y) - (1 - y)*(5 + 9*y - 6*y**2)))

gosaminfo = False
if(gosaminfo is True):
    print("   real(ki) :: mW =       "+str(mw)+"_ki")
    for mt in [165.0,172.5,180.0]:
        print("   real(ki) :: mT =      "+str(mt)+"_ki")
        for scale in [0.5,1.0,2.0]:
            print("scale="+str(scale)+":")
            print("   real(ki) :: wT =        "+str(gammaT("BVI",mt,scale))+"_ki")
            print("   real(ki) :: wW =        "+str(gammaW("BVI",mt,scale))+"_ki")
        print("___________________________________________")
    exit()


if part == "BVIRS":
    part = ""

sherpaopts = [ "TMASS:="+str(TMASS),
               "TWIDTH:="+str(gammaT(part,TMASS,scalefac)),
               "WWIDTH:="+str(gammaW(part,TMASS,scalefac)),
               "MYSCALEFAC:="+str(scalefac),
               "tgerr:="+str(err), 
               "-f", "Run_"+part+".dat" ]
fileidentifier = "_"+part+"_"+str(TMASS)+"_"+str(scalefac)

if mode == "grid":
	process = Popen( [ "sbatch"], stdin = PIPE )
        process.stdin.write('#!/bin/sh\n')
        process.stdin.write('#SBATCH --error="slurm'+str(TMASS)+'.err"\n')
        process.stdin.write('#SBATCH --output="slurm'+str(TMASS)+'.out"\n')
	process.stdin.write('#SBATCH -J grid\n')
	process.stdin.write('#SBATCH --partition=broadwell\n')
	process.stdin.write('#SBATCH --nodes=1\n')
	process.stdin.write('#SBATCH --ntasks-per-node=40\n')
	process.stdin.write('#SBATCH --time=24:00:00\n')
	process.stdin.write('export PATH=/ptmp/lscyboz/SHERPA-MC-2.2.2/bin/:$PATH\n')
        process.stdin.write(' '.join(['srun', 'Sherpa'] + sherpaopts)+'\n')
        process.stdin.write('exit 0\n')
        process.stdin.close()
#    with open( "sherpa"+fileidentifier+".log", "a+" ) as outfile:
#        process = Popen( ["nohup","mpirun","-n",str(mpithreads),"Sherpa"] + sherpaopts, stdout=outfile )

elif mode == "event":
    if submit == 'serial':
        with open( "sherpa"+fileidentifier+".log", "a+" ) as outfile:
            process = Popen( ["Sherpa"] + sherpaopts, stdout=outfile )
    elif submit == 'slurm':
     for i in range(n):
        process = Popen( [ "sbatch"], stdin = PIPE )
        process.stdin.write('#!/bin/sh\n')
#        process.stdin.write('#SBATCH --array='+str(nstart)+'-'+str(nstart+n-1)+'\n')
        process.stdin.write('#SBATCH --error="slurm-%A_%a.err"\n')
        process.stdin.write('#SBATCH --output="slurm-%A_%a.out"\n')
        process.stdin.write('#SBATCH --job-name="evt_'+str(TMASS)+'_'+str(i)+'"\n')
        process.stdin.write('#SBATCH --partition=broadwell\n')
        process.stdin.write('#SBATCH --nodes=1\n')
        process.stdin.write('#SBATCH --ntasks-per-node=40\n')
        process.stdin.write('#SBATCH --time=24:00:00\n')
	process.stdin.write('source /ptmp/lscyboz/RIVET-2.5.1/rivetenv.sh\n')
	process.stdin.write('export RIVET_ANALYSIS_PATH=/ptmp/lscyboz/RivetCustomAnalyses:$RIVET_ANALYSIS_PATH\n')
	process.stdin.write('export PATH=/ptmp/lscyboz/SHERPA-MC-2.2.2/bin/:$PATH\n')
#	process.stdin.write('srun Sherpa -f Run_wwbb.dat -e 1000000 -A 06.04.17.\n')
        process.stdin.write(' '.join(['srun', 'Sherpa',' random1:=1$SLURM_JOB_ID'] + sherpaopts)+'\n')
        process.stdin.write('exit 0\n')
        process.stdin.close()
    elif submit == 'condor':
        process = Popen( [ "condor_submit"], stdin = PIPE )
        process.stdin.write('#!/usr/bin/env condor_submit\n')
        process.stdin.write('Universe = vanilla\n')
        process.stdin.write('Executable = '+str(check_output(['which','Sherpa']))+'\n')
        process.stdin.write('Notification = Never\n')
        process.stdin.write('Input = /dev/null\n')
        process.stdin.write('Output = condor'+fileidentifier+'.$(Cluster).$(Process)-stdout.txt\n')
        process.stdin.write('Error = condor'+fileidentifier+'.$(Cluster).$(Process)-stderr.txt\n')
        process.stdin.write('Log = condor'+fileidentifier+'.$(Cluster).$(Process)-stdlog.txt\n')
        process.stdin.write('Getenv = true\n')
        process.stdin.write('Requirements = Arch == "X86_64" && Pool == "Theory" && Distro == "openSUSE" && (Machine != "pcl343.mppmu.mpg.de")\n')
        process.stdin.write('Initialdir = '+getcwd()+'\n')
        for ran in range(nstart, nstart + n ):
            process.stdin.write(' '.join(['Arguments  = "-o 0 random:=1'+str(ran)] + sherpaopts + ['"'])+'\n')
            process.stdin.write('Queue\n\n')
        process.stdin.close()


