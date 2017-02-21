FLAGS=
LIBS=

ABS=/ptmp/lscyboz/HERWIG/Herwig-scratch/Build/GoSam/source/

for file in $(find . -maxdepth 1 -type d -name "p*") #or you can use the awk one here
 
do

FLAGS+="-I $ABS${file:2}/common -I $ABS${file:2}/matrix -L $ABS${file:2}/.libs "
LIBS+="$ABS${file:2}/common/.libs/libgolem_process_${file:2}_common.so $ABS${file:2}/matrix/.libs/libgolem_process_${file:2}_matrix.so "

done
echo $FLAGS
echo "\n"
echo $LIBS

