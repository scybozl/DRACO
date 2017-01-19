import os
sampledPars = "/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/"
selecPath   = "/ptmp/lscyboz/processSelection.in"

def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def createSubmit(directory):

    os.system("cd /ptmp/lscyboz/")

    template=open("submit_GoSam.sh", 'r')
    fileName="Submit_"+name+".sh"
    file=open(fileName, 'w')

    for line in template:
	if line.find("cd")!=-1:
	  file.write("cd "+directory)
	else:
	  file.write(line) 


for subdir in SubDirPath(sampledPars):
    if subdir.find('nmubarep')!=-1:
      for hel in SubDirPath(subdir):
	if hel.find("helicity")!=-1:

		name=hel.split("source/")[1].split("/")[0]+"_"+hel.split("source/")[1].split("/")[1]
		selec=open(selecPath, 'r')
		for line in selec:
		  if name.find(line.split("\n")[0])!=-1:
		    createSubmit(hel)
		    os.system("sbatch Submit_"+name+".sh")
#    os.system("./yoda2aida "+subdir+"/out.yoda "+subdir+"/out.aida")
