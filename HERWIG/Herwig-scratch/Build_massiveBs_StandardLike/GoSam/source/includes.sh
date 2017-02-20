FLAGS=

for file in $(find . -maxdepth 1 -type d -name "p*") #or you can use the awk one here
 
do

FLAGS+="-I $file/common -I $file/matrix "


done
echo $FLAGS
