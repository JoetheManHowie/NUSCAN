# Python scripts
---------------

This directory contains scripts that are designed to test whether a dataset meets the requirements for a graph to successfully on USCAN and NUSCAN.
The requirements are listed below.


# Dataset Requirements
-----------------------

USCAN and NUSCAN are both algorithms designed to operate on undirected probabilistic graphs. As implemented, the C++ code requires the graphs to be formatted in a particular fashion. For USCAN and NUSCAN to run with out faults, the following properties must be true:

1. the graph is saved to a text file as a edgelist, with every line reading $u$  $v$  $p$ where any amount of whitespace separating the numbers.
5. if the edge $u$  $v$  $p$ is in the graph, then both it and the reverse edge $v$  $u$  $p$ are present in the edgelist.
2. $p$ is a decimal number on the open interval between 0 and 1.
3. the edgelist is doubly sorted, first by $u$ then by $v$.
4. $u$ and $v$ are integers that range from $0$ to $n-1$, where $n = |V|$ (number of vertices in the graph).


Note that both algorithms are for undirected graph but we need to include reverse edges, this is because of the data structure that stores the nodes and their neighbours. Additionally, if any vertices in the $0$ to $n-1$ are not present, the graph with not run on the implemented code.


## Checking code
-----------------

For uscan and nuscan to be able to process graph they need to meet the following requirements.


## Modifying code
---------------


## Our method
---------------

+ All the datasets we worked with were found in the edgelist form and some had probabilities to start, satifying requirement 1.
+ We check that the graph is symmetric using `check_symmetry.py`, and if is not symmetric we run the graph through `make_symmetric.py` to satisfy requirement 2.
+ Next `range_p_check.py` determines which edges, if any, have probabilities of zero or one. Then `perturb_p_bounds.py` adjusts any $0$ or $1$ weights to $0.001$ and $0.999$ respectively, satisfying requirement 3.
+ Then by running the bash command `sort -o -n -k1,2 <graph.txt>` the graph becomes sorted by the firstcolumn and then by the second column, satifying requirement 4.
+



## Adding Probabilities
------------------------

