# Python scripts
---------------

This directory contains scripts that are designed to test whether a dataset meets the requirements for a graph to successfully on USCAN and NUSCAN.
The requirements are listed below.

Every `.py` file in this directory are executables and take one command line argument, the path to the graph.

`./<python executable> <path to graph>`

## Python dependencies
-----------------------
The scripts in this directory use the following pip installable modules:

`pip install numpy`

Along with modules in the python standard library.

# Dataset Requirements
-----------------------

USCAN and NUSCAN are both algorithms designed to operate on undirected probabilistic graphs. As implemented, the C++ code requires the graphs to be formatted in a particular fashion. For USCAN and NUSCAN to run with out faults, the following properties must be true:

0. The graph is saved to a text file as an edgelist, with every line reading $u$  $v$  $p$ where any amount of whitespace separating the numbers.
1. If the edge $u$  $v$  $p$ is in the graph, then both it and the reverse edge $v$  $u$  $p$ are present in the edgelist.
2. $p$ is a decimal number on the open interval between 0 and 1.
3. The edgelist is doubly sorted, first by $u$ then by $v$.
4. Remove all self loops.
5. $u$ and $v$ are integers that range from $0$ to $n-1$, where $n = |V|$ (number of vertices in the graph).


Note that both algorithms are for undirected graph but we need to include reverse edges, this is because of the data structure that stores the nodes and their neighbours. Additionally, if any vertices in the $0$ to $n-1$ are not present, the graph with not run on the implemented code.


## Checking code
-----------------

The following `.py` files are used to check requirements 1 through 5:

1. [`symmetry_check_step1.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/symmetry_check_step1.py)
2. [`p_check_step2.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/p_check_step2.py)
3.  _not implemented_
4. [`self_loop_check_step4.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/self_loop_check_step4.py)
5. [`numbering_check_step5.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/numbering_check_step5.py)

We did not write a program to check if the graphs were sorted (step 3) since we sorted them with the bash command `sort`.

## Modifying code
---------------

The following `.py` files are used to apply requirements 1 through 5:

1. [`make_symmetric_step1.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/make_symmetric_step1.py)
2. `p_bounds_step2.py` _-- not implemented, since none of our graphed required such a function._
3. [`doubly_sort_step3.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/doubly_sort_step3.py)
4. [`doubly_sort_step3.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/remove_self_loops_step4.py) _-- implemented, but never needed._
5. [`fix_missing_nodes_step5.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/fix_missing_nodes_step5.py)

# Our method
---------------
The step numbers here correspond to the requirement numbers above.

0. All the datasets we worked with were found in the edgelist form and some had probabilities to start.
1. We check that the graph is symmetric using `symmetry_check_step1.py`, and if is not symmetric we run the graph through `make_symmetric_step1.py`.
2. Next `p_check_step2.py` determines which edges, if any, have probabilities of zero or one. Then `p_bounds_step2.py` adjusts any $0$ or $1$ weights to $0.001$ and $0.999$ respectively.
3. Then by running `doubly_sort_step3.py` the graph becomes sorted by the first column and then by the second column.
4. Any self loops found with `self_loop_check_step4.py` are removed from the graph with `remove_self_loops_step4.py`.
5. Finally, `numbering_check_step5.py` to determine if any vertex indices are missing, and if there are correct the numbering with `fix_missing_nodes_step5.py`. Note if the original numbering is important to the data, add a `True` flag to the command for `fix_missing_nodes_step5.py` and a pickle file will be saved to the same directory and the new graph file that holds the mapping of nodes.


## Adding Probabilities
------------------------

There are some large datasets that we used in experiments that did not have probability weights. In these cases we induces probabilities from different probability distribution functions (PDFs). In these cases we have written a python script for step 0, that takes an edgelist text file and adds probabilities to the edges.

We used the executable [`alter_weights_step0.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/prep_graph/alter_weights_step0.py) to read graph files that were already processed, and change the weights to be from specific probability distribution without altering any of the 5 requirements.

The python code takes three arguments,

`./alter_weights_step0.py <path> <graph> <distribution>`

and returns a graph file with the new weights. So if the name of the input graph was `graph.txt` and you ran `./alter_weights_step0.py ./ graph.txt normal` would produce a graph called `graph.normal` in the directory `<path>`.

Note: Only three distributions have been implemented:

+ power law (Key: `exp`)
+ normal (Key: `normal`)
+ uniform (Key: `uniform`)

Additionally, there is a v2 of alter_weights_step0.py that uses random.uniform instead of np.random.rand. 
