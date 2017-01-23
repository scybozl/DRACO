import os
sampledPars = "/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/"

def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def createSubmit(i):

    os.system("cd /ptmp/lscyboz/")

    template=open("submit_HERWIG.sh", 'r')
    fileName="Submit_"+str(i)+".sh"
    file=open(fileName, 'w')

    for line in template:
	if line.find("Herwig integrate")!=-1:
	  file.write("Herwig integrate --jobid="+str(i)+" emubB_matchbox_NLO.run -d 9")	
	else:
	  file.write(line) 


for k in range(0,17):
#	if k!=28:
	  createSubmit(k)
	  os.system("sbatch Submit_"+str(k)+".sh")
#    os.system("./yoda2aida "+subdir+"/out.yoda "+subdir+"/out.aida")
