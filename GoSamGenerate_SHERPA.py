import os
sampledPars = "/ptmp/lscyboz/SHERPA-MC-2.2.0/emubB/Virtual/"

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
    if subdir.find('epnemum')!=-1:
	createSubmit(subdir.split("Virtual/")[1])
	os.system("sbatch Submit_"+subdir.split("Virtual/")[1]+".sh")
#    os.system("./yoda2aida "+subdir+"/out.yoda "+subdir+"/out.aida")
