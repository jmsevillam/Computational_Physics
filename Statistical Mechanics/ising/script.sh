for i in `seq 10 10 100`
do
  echo $i
  time ./ising.out $i $1 $2 > $i.dat
done
