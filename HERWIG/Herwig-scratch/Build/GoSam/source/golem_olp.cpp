#include<iostream>
#include<dlfcn.h>
#include<stdio.h>

using namespace std;
__attribute__((constructor)) void golem_olp(void)
{
  void *handle[18];
  handle[0] = dlopen("/ptmp/lscyboz/HERWIG/lib/libff.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[1] = dlopen("/ptmp/lscyboz/HERWIG/lib/libavh_olo.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[2] = dlopen("/ptmp/lscyboz/HERWIG/lib/libqcdloop.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[3] = dlopen("/ptmp/lscyboz/HERWIG/lib/libsamurai.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[4] = dlopen("/ptmp/lscyboz/HERWIG/lib/libninja.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[5] = dlopen("/ptmp/lscyboz/HERWIG/lib/libgolem.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[6] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p0_ddbar_emep/common/libgolem_process_p0_ddbar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[7] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p18_gg_nmubarepbbarbnemum/libgolem_process_p18_gg_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[8] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p12_ubaru_nmubarepbbarbnemum/libgolem_process_p12_ubaru_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[9] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p0_ddbar_nmubarepbbarbnemum/libgolem_process_p0_ddbar_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[10] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p10_ddbar_nmubarepbbarbnemum/libgolem_process_p10_ddbar_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[11] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p16_sbars_nmubarepbbarbnemum/libgolem_process_p16_sbars_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[12] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p4_ccbar_nmubarepbbarbnemum/libgolem_process_p4_ccbar_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[13] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p2_ubaru_nmubarepbbarbnemum/libgolem_process_p2_ubaru_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[14] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p6_sbars_nmubarepbbarbnemum/libgolem_process_p6_sbars_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[15] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p8_gg_nmubarepbbarbnemum/libgolem_process_p8_gg_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[16] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/p14_ccbar_nmubarepbbarbnemum/libgolem_process_p14_ccbar_nmubarepbbarbnemum.so",RTLD_LAZY|RTLD_GLOBAL);
  handle[17] = dlopen("/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/libolp_module.so", RTLD_LAZY|RTLD_GLOBAL);
  for(int i=0; i<=36; i++){
  if (!handle[i])
    {
     printf("The error is %s \n", dlerror());

    }
  else
   {
    printf("Library loaded \n");
   }
  }

return ;
};

