
#! /usr/bin/python

import os
from time import gmtime, strftime
import glob

nEvPerFile = 10000
nRuns = 1000

dir = "/ptmp/lscyboz/Herwig_WWbB_"+strftime("H:%M:%S", gmtime())+"/"
InputFolder = "/ptmp/lscyboz/HERWIG/"
WorkFolder = "/ptmp/lscyboz"

SettingsFolder    = "/ptmp/lscyboz/Settings/"
SetupFileNameGen    = "setupfile.in"

pars 		= "/afs/ipp-garching.mpg.de/home/l/lscyboz/mc/"

def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def printSetupLinesInSubmitFileRivet(file):

#    setupLines = ["export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/ \n",
#                  "source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh \n",
#                  "asetup 20.8.2 \n"
#                  ]

    setupLines = ["source /ptmp/lscyboz/Herwig-7.0.3/bin/activate\n",
		  "source /afs/ipp-garching.mpg.de/home/l/lscyboz/Herwig-7.0.3/src/Rivet-2.4.0/rivetenv.sh\n",
		  "export RIVET_ANALYSIS_PATH=/afs/ipp-garching.mpg.de/home/l/lscyboz/RivetCustomAnalyses/:$RIVET_ANALYSIS_PATH\n"]

    file.writelines(setupLines)

def initRun():

    os.system("chmod a+x initRun.sh")
    os.system("./initRun.sh")
    

def SubmitHerwigJob(nEvents, seed, InputFileNameGen):

    specStr          = '%03.0f' % (seed,)
#    tmpFolder        = dir+specStr+"/"
    OutputFile       = "seed_"+specStr+".hepmc"
    OutputFolder     = dir+specStr+"/"
    OutputYoda        = OutputFolder+"seed_"+specStr+".yoda"
    tmp              = "$TMPDIR/lscyboz/"+specStr+"/"

#    os.system("mkdir -p "+OutputFolder)

    OutputFileFinal  = OutputFolder+OutputFile

    submitFileNameSH = WorkFolder+"Event_"+specStr+".sh"

    redo = false
    if os.path.exists(OutputYoda):
      f=open(OutputYoda,'r')
      for i, line in enumerate(f):
        if "END YODA_COUNTER" in line:
              number=i
      f=open(OutputYoda,'r')
      string=f.readlines()[number-1]
      nE=float(string.split("\t")[2].split("\n")[0])
      if nE!=nEvents:
        redo = True
    else: redo = True
    os.chdir(OutputFolder)

    if redo==True:

        submitfile2 = open(submitFileNameSH, "w")
        printSetupLinesInSubmitFileRivet(submitfile2)

        codeLines2 = []
#       codeLines2.append("mkdir -p "+tmpFolder)
        codeLines2.append("cd "+InputFolder)
        codeLines2.append("mkdir -p "+tmp)
        codeLines2.append("echo 'set /Herwig/Generators/EventGenerator:RandomNumberGenerator:Seed "+str(seed)+"' >> "+OutputFolder+SetupFileNameGen)
        codeLines2.append("echo \"set /Herwig/Analysis/HepMCFile:Filename "+tmp+OutputFile+"\" >> "+OutputFolder+SetupFileNameGen)

        codeLines2.append("Herwig run "+InputFileNameGen+" -N "+str(nEvents)+" -x "+OutputFolder+SetupFileNameGen)

        analyses=""
                analyses += " -a "+routines

        for codeLine in codeLines2:
            submitfile2.write(codeLine+" \n")

        submitfile2.write("rm "+ submitFileNameSH + " \n")
        submitfile2.write("rm -r "+ tmp + " \n")
        submitfile2.close()

        cmd = "chmod a+x " + submitFileNameSH
        os.system(cmd)
        cmd = "sbatch "+ submitFileNameSH
        os.system(cmd)

        return True

    else:
        return False


## Options file for systematic generation: the user should set the settings required for the different runs there

os.system("source /ptmp/lscyboz/Rivet-2.5.0/rivetenv.sh")
os.system("export RIVET_ANALYSIS_PATH=/ptmp/lscyboz/RivetCustomAnalyses/:$RIVET_ANALYSIS_PATH")


## Submit the job to Herwig
for i in range(nRuns):
	spec='%03.0f' % (i,)
	if not os.path.exists(dir+spec):
	  os.system("mkdir -p "+dir+spec)
	os.system("cp "+InputFolder+"emubB_homemade_NLO.in "+dir)
	if (i+1)%100==0: print "Processing run #"+str(i)

	SubmitHerwigJob(nEvPerFile, i, "emubB_matchbox_NLO.run")

	if (i+1)%400==0:
		while True:
		  os.system('squeue -u lscyboz > file')
                  strn=open('file', 'r').read()
           	  if len(strn) <= 800: break
                  time.sleep(15)
                  print "."
                print "\n"
	if (i+1)%400==0:
                while True:
                  os.system('squeue -u lscyboz > file')
                  strn=open('file', 'r').read()
                  if len(strn) <= 800: break
                  time.sleep(15)
                  print "."
                print "\n"

## Yoda-merge the files from the different runs 
print "Yoda-merging at generated cross-section"
os.system("yodamerge "+dir+"*/*"+norms+".yoda -o "+dir+"MC_Herwig_"+settings+"_unnorm.yoda")

os.system("cp "+dir+"MC_Herwig_"+settings+"*.yoda "+subdir)

