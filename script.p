set term epslatex color size 8cm, 5cm
set output 'connect.tex'
#set multiplot layout 1, 2
#set grid
set xlabel '$1/N$'
set ylabel '$\mathcal{N}_4/\mathcal{N}_4^{(f)}$'
plot 'tetrads_R1.dat' w lp lt 7 notitle, 2*x lc "blue" title 'Eq. \eqref{conFMC}'
