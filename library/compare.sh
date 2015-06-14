

while :
do
    python gen.py > tmp.out
    python naive.py < tmp.out > naive.out
    python C.py < tmp.out > alg.out
    
    if diff naive.out alg.out > /dev/null; 
    then
	echo "pass one test"
    else
	echo "input"
	cat tmp.out
	echo "naive"
	cat naive.out
	echo "algorithm"
	cat alg.out
	exit
    fi
done


