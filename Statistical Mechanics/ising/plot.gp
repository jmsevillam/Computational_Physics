plot '10.dat' u 1:2:3 w yerr,'20.dat' u 1:2:3 w yerr,'30.dat' u 1:2:3 w yerr,'40.dat' u 1:2:3 w yerr,'50.dat' u 1:2:3 w yerr,'60.dat' u 1:2:3 w yerr,'70.dat' u 1:2:3 w yerr,'80.dat' u 1:2:3 w yerr,'90.dat' u 1:2:3 w yerr,'100.dat' u 1:2:3 w yerr
set term png
set output 'magne_all.png'
replot
set term qt
reset

plot '10.dat' u 1:4 w lp,'20.dat' u 1:4 w lp,'30.dat'u 1:4 w lp,'40.dat' u 1:4 w lp,'50.dat' u 1:4 w lp,'60.dat' u 1:4 w lp,'70.dat' u 1:4 w lp,'80.dat' u 1:4 w lp,'90.dat' u 1:4 w lp,'100.dat' u 1:4 w lp
set term png
set output 'sus_all.png'
replot
set term qt
reset

plot '10.dat' u 1:4,'20.dat' u 1:4,'30.dat' u 1:4,'40.dat' u 1:4,'50.dat' u 1:4,'60.dat' u 1:4,'70.dat' u 1:4,'80.dat' u 1:4,'90.dat' u 1:4,'100.dat' u 1:4
set term png
set output 'sus_all_log.png'
set logscale y
replot
set term qt
