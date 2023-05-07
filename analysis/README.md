# Analysis
--------------

In our paper, *Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem* we preformed a series of experiments on different datasets. In this directory we have provided code for reproducing these experiments with some python scripts that read the output files from nuscan and uscan.

## Experiments
----------------

In Section 4 of our paper we outline four different experiments to test the efficiency, scalability, accuracy, and effectiveness of the NUSCAN algorithm. In this directory we have python scripts that generate outputs from the output files of [`uscan`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) and [`nuscan`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) and the formatted graph file.

### Graph Properties

The script [`metrics.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/metrics.py) prints the folloing information about the graph:

`<number of vertices> <number of edges> <cluster coefficient of deterministic graph> <maximum degree> <average degree>`

and to run the command in the terminal type `./metrics <path to formatted graph>`

### Comparing NUSCAN and USCAN clusterings

To compare the cluster sets, hubs, outliers, cores, and non-cores we run the script [`cluster_compare.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/cluster_compare.py) that prints out 