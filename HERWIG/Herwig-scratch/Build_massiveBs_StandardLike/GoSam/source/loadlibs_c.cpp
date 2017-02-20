#include<iostream>
#include<dlfcn.h>
#include<stdio.h>

using namespace std;
__attribute__((constructor)) void loadlibs(void)
{
  void *handle[37];
  handle[0] = dlopen("/home/ttp/greiner/local/lib64/libff.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[1] = dlopen("/home/ttp/greiner/local/lib64/libavh_olo.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[2] = dlopen("/home/ttp/greiner/local/lib64/libqcdloop.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[3] = dlopen("/home/ttp/greiner/local/lib64/libsamurai.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[4] = dlopen("/home/ttp/greiner/local/lib64/libninja.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[5] = dlopen("/home/ttp/greiner/local/lib64/libgolem.so",  RTLD_LAZY|RTLD_GLOBAL);
  handle[6] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/common/libgosam_process_p0_ddbar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[7] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/helicity0/libgosam_process_p0_ddbar_emep_amplitude0.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[8] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/helicity1/libgosam_process_p0_ddbar_emep_amplitude1.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[9] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/helicity2/libgosam_process_p0_ddbar_emep_amplitude2.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[10] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/helicity3/libgosam_process_p0_ddbar_emep_amplitude3.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[11] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p0_ddbar_emep/matrix/libgosam_process_p0_ddbar_emep_matrix.so", RTLD_LAZY|RTLD_GLOBAL);

  handle[12] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/common/libgosam_process_p2_uubar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[13] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/helicity0/libgosam_process_p2_uubar_emep_amplitude0.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[14] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/helicity1/libgosam_process_p2_uubar_emep_amplitude1.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[15] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/helicity2/libgosam_process_p2_uubar_emep_amplitude2.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[16] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/helicity3/libgosam_process_p2_uubar_emep_amplitude3.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[17] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p2_uubar_emep/matrix/libgosam_process_p2_uubar_emep_matrix.so", RTLD_LAZY|RTLD_GLOBAL);

  handle[18] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/common/libgosam_process_p4_ssbar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[19] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/helicity0/libgosam_process_p4_ssbar_emep_amplitude0.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[20] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/helicity1/libgosam_process_p4_ssbar_emep_amplitude1.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[21] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/helicity2/libgosam_process_p4_ssbar_emep_amplitude2.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[22] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/helicity3/libgosam_process_p4_ssbar_emep_amplitude3.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[23] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p4_ssbar_emep/matrix/libgosam_process_p4_ssbar_emep_matrix.so", RTLD_LAZY|RTLD_GLOBAL);

  handle[24] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/common/libgosam_process_p6_ccbar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[25] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/helicity0/libgosam_process_p6_ccbar_emep_amplitude0.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[26] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/helicity1/libgosam_process_p6_ccbar_emep_amplitude1.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[27] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/helicity2/libgosam_process_p6_ccbar_emep_amplitude2.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[28] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/helicity3/libgosam_process_p6_ccbar_emep_amplitude3.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[29] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p6_ccbar_emep/matrix/libgosam_process_p6_ccbar_emep_matrix.so", RTLD_LAZY|RTLD_GLOBAL);

  handle[30] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/common/libgosam_process_p8_bbbar_emep_common.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[31] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/helicity0/libgosam_process_p8_bbbar_emep_amplitude0.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[32] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/helicity1/libgosam_process_p8_bbbar_emep_amplitude1.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[33] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/helicity2/libgosam_process_p8_bbbar_emep_amplitude2.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[34] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/helicity3/libgosam_process_p8_bbbar_emep_amplitude3.so", RTLD_LAZY|RTLD_GLOBAL);
  handle[35] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/p8_bbbar_emep/matrix/libgosam_process_p8_bbbar_emep_matrix.so", RTLD_LAZY|RTLD_GLOBAL);

  handle[36] = dlopen("/data/greiner/testgosam/test_olp/virtual_ppee_qcd/libolp_module.so", RTLD_LAZY|RTLD_GLOBAL);
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

