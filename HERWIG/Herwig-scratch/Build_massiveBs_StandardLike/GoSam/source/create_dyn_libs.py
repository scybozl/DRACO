#!/usr/bin/python

import sys
import os
import subprocess


if __name__ == "__main__":
    maindir=os.getcwd()
    #dir=maindir+'/'+sys.argv[1]
    #print dir
    #os.chdir(dir+'/common')
    #subprocess.Popen('g++ -shared -Wl,--whole-archive common.a -o common.so -Wl,--no-whole-archive', shell=True,stdout=subprocess.PIPE).wait()
    #os.chdir(dir+'/matrix')
    #subprocess.Popen('g++ -shared -Wl,--whole-archive matrix.a -o matrix.so -Wl,--no-whole-archive', shell=True,stdout=subprocess.PIPE).wait()    
    #os.chdir(dir)
    #helicitylist = subprocess.Popen('ls -d helicity*', shell=True, stdout=subprocess.PIPE).communicate()[0]
    #helicities=helicitylist.split('\n')
    #del helicities[-1]
    
    #for helicity in helicities:
        #print helicity
        #number=helicity.split('helicity')[1]
        #os.chdir(dir+'/'+helicity)
        #subprocess.Popen('g++ -shared -Wl,--whole-archive amplitude'+number+'.a -o amplitude'+number+'.so -Wl,--no-whole-archive', shell=True,stdout=subprocess.PIPE).wait()    
        
    #os.chdir(maindir)
    
    fullist=''
    subprocess.Popen('ar rcs olp_module.a olp_module.o',shell=True).wait()
    proclist = subprocess.Popen('ls -d p*', shell=True, stdout=subprocess.PIPE).communicate()[0]
    processes=proclist.split('\n')
    del processes[-1]
    
    for process in processes:
        print process
        fullist = fullist + maindir+'/'+process+'/common/common.a '+ maindir+'/'+process+'/matrix/matrix.a '
        os.chdir(maindir+'/'+process)
        helicitylist = subprocess.Popen('ls -d helicity*', shell=True, stdout=subprocess.PIPE).communicate()[0]
        helicities=helicitylist.split('\n')
        del helicities[-1]
    
        for helicity in helicities:
            print helicity
            number=helicity.split('helicity')[1]        
            fullist=fullist+ maindir+'/'+process+'/'+helicity+'/amplitude'+number+'.a '
            
        os.chdir(maindir)
        
    fullist = fullist + maindir+'/olp_module.a'
            
    subprocess.Popen('g++ -shared -Wl,--whole-archive '+fullist+' -o libgolem.so -Wl,--no-whole-archive', shell=True,stdout=subprocess.PIPE).wait()    
    
