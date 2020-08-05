number = 1000
number2 = 5000
CC = g++-9
target:
	${CC} Model.cpp -O3 -ffast-math -o ising.out
run:
	time ./script.sh ${number} ${number2}
plot:
	gnuplot plot.gp
clean:
	@-rm *.dat
	@-rm plot_all.pdf
	rm ising.out
