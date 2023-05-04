# Python Script
----------------
This directory contains scripts that are designed to test whether a dataset meets the requirements for a graph to successfully on USCAN and NUSCAN.
The requirements are listed in the [`datasets/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/datasets) directory.

## Checking code
-----------------

For uscan and nuscan to be able to process graph they need to meet the following requirements.


## Modifying code
---------------


## Our method
---------------

+ All the datasets we worked with were found in the edgelist form and some had probabilities to start, satifying requirement 1 in [`datasets/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/datasets). See the section below on adding probabilities for the cases where probabilities are not provided.
+ We check that the graph is symmetric using `check_symmetry.py`, and if is not symmetric we run the graph through `make_symmetric.py` to satisfy requirement 2 in [`datasets/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/datasets).
+ Next `range_p_check.py` determines which edges, if any, have probabilities of zero or one. Then `perturb_p_bounds.py` adjusts any $0$ or $1$ weights to $0.001$ and $0.999$ respectively, satisfying requirement 3 in [`datasets/`](\https://github.com/JoetheManHowie/NUSCAN/tree/main/datasets).
+ Then by running the bash command `sort -o -n -k1,2 <graph.txt>` the graph becomes sorted by the firstcolumn and then by the second column, satifying requirement 4 [`datasets/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/datasets).
+



## Adding Probabilities
------------------------

