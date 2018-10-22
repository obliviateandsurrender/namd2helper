j=2.00
l=4.00
mkdir -p result
for i in $(seq 4.00 2.00 30.00)
do
    k=`echo $i + $j | bc`
    n="./result/nacl_us_${i%.*}.log"
    o="./result/nacl_us_${i%.*}.colvars.traj" 
    namd2 nacl.namd > $n
    mv ./nacl_us.colvars.traj $o
    sed -i "s/${i}/${k}/g" colvars.conf
done
sed -i "s/${k}/${l}/g" colvars.conf
