import os

def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

file = open("listDir.in", 'w')
num = 6

for dir in SubDirPath("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build_massiveBs_StandardLike/GoSam/source/"):

    if dir.find("source/p")!=-1:
#	print dir

#	for f in os.listdir(dir+"/common"):
#	  if f.find(".so") != -1:
#	    print f

#	for f in os.listdir(dir+"/matrix"):
#	  if f.find(".so") != -1:
#	    print f

#	for f in os.listdir(dir):
#	  if f.find("helicity") != -1:
#	    for i in os.listdir(dir+"/"+f):
#		if i.find(".so") != -1:
#		  print i

	for f in os.listdir(dir):
	  if f.find("nmubarepbbarbnemum.so") != -1:
		  num += 1
		  print f
		  file.write("  handle["+str(num)+"] = dlopen(\""+dir+"/"+f+"\",RTLD_LAZY|RTLD_GLOBAL);\n")


file.close()
