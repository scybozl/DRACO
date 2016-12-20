import os
sampledPars = "/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/"

def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def createSubmit(directory):

    os.system("cd /ptmp/lscyboz/")

    template=open("submit_GoSam.sh", 'r')
    fileName="Submit_"+directory+".sh"
    file=open(fileName, 'w')

    for line in template:
	if line.find("cd")!=-1:
	  file.write("cd "+sampledPars+directory)
	else:
	  file.write(line) 


for subdir in SubDirPath(sampledPars):
    if subdir.find('nmubarepbbar')!=-1:
	createSubmit(subdir.split("source/")[1])
	os.system("sbatch Submit_"+subdir.split("source/")[1]+".sh")
#    os.system("./yoda2aida "+subdir+"/out.yoda "+subdir+"/out.aida")
