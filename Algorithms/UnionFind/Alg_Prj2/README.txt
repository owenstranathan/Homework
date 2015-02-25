This is a project made by Owen Stranathan

The program contained in percolate.cpp is a c++ source file. 
The program should be compiled with the following command

    g++ percolate.cpp -o <NAME>

the program can then be run according to these guidelines

to run the program using a file
use the following commad

    ./<NAME> <FILENAME>.txt

The output will be the number of clusters in the file

to run using a probability 
use the following command

    ./<NAME> <PROBABILITY> <#RUNS> <MATRIXSIZE>

the output will be the percolation rate. 


The point of this program is to utilize UnionFind Algorithm to determine the
stochastic percolation threshold of a square matrix.
