import glob

for files in glob.glob("*.yoda"):
        f=open(files,'r')
        for i, line in enumerate(f):
          if "BEGIN YODA_HISTO1D /MC_MARKUS13TEV/xs\n" in line:
                number=i
	f=open(files,'r')
        string=f.readlines()[number+8]
        nE=int(string.split("\n")[0].split("\t")[6])
	if nE!=5000000:
	  print files
