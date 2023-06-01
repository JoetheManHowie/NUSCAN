# nuscan
--------------
Here is the C++ code for the NUSCAN clustering algorithm. The code can be modified and integrated with other C++ applications. The algorithm is composed of four .cpp files and four .h files.

+ [`Edge.h`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Edge.h) and [`Edge.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Edge.cpp)
+ [`Graph.h`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Graph.h) and [`Graph.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Graph.cpp)
+ [`Node.h`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Node.h) and [`Node.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Node.cpp)
+ [`Util.h`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Util.h) and [`Util.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Util.cpp)

Then the .cpp file [`main.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/main.cpp) gives an example of how to execute the clustering framework. We compile all these classes together and make the executable called [`nuscan`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/nuscan) which runs the [`main.cpp`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/main.cpp) file.


## Compiling
------------

In order to compile the nuscan algorithm, download the code in this directory and have a properly formatted graph (see [`prep_graph`](https://github.com/JoetheManHowie/NUSCAN/tree/main/prep_graph)). Then in the terminal run the `make` command; this executes the code in the [`Makefile`](https://github.com/JoetheManHowie/NUSCAN/blob/main/nuscan/Makefile) which compile the .cpp files so that main is the executed file using -03 optimization.


## Execution
------------

To run the clustering algorithm and produce the `.cluster_nuscan` and `.prob_nuscan` files, run the following command with all parameters.

`./nuscan <path-to-graph-file> <eta> <eps> <mu> <thres> output`

The presence of the string `output` will make the program create the two output files in the same directory as the input graph. The code it self will print out to the terminal the following:

`<eta> <eps> <mu> <thres> <time-to-cluster> <number-of-core> <number-of-clusters> <number-of-hubs> <number-of-outliers>`

### Remarks
-----------
Special thanks to the author of [Qiu et. al.](https://ieeexplore.ieee.org/abstract/document/8476242) for providing their source code for [`uscan`](https://github.com/JoetheManHowie/NUSCAN/blob/main/uscan/) upon which the nuscan framework was implemented.
