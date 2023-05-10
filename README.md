# Introduction
--------------------

This repository contains all the code and instructions neccessary to reproduce the experimental results from our paper "Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem".


## Overview
------------

There are five directories each with their our purpose:

1. [`prep_graphs/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/prep_graph) contains all the python code used to format datasets for the clustering algorithms NUSCAN and USCAN.
1. [`uscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) holds the C++ implementation of USCAN as coded by the authors, with few additions needed for our analysis.
1. [`nuscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) holds the modified USCAN code that includes the NUSCAN algorithm.
1. [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis) has the scripts used to analyze the clusters and probability calculations made by both algorithms.
1. [`visualization`](https://github.com/JoetheManHowie/NUSCAN/tree/main/visualization) makes plots that visualize the results of the clustering algorithms and metric comparisons.

In each of these directory there are more specific instructions for using the code inside.


## Workflow
--------------

In general to execute the analysis that was done in our paper the following sets must take place:

1. Format graph - NUSCAN and USCAN both operate on undirected probabilistic graphs. See [`prep_graphs/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/prep_graph) for more information on the formatting requirements.
2. Run the graph through both clustering algorithms with the output option to generate the txt files with the probabilities $P[e, \varepsilon]$ for each e and another txt file with the cluster sets, hubs, and outliers. See [`uscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) and [`nuscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) for more details.
3. Analyze results - there are some scripts that compute cluster quality, compare $P[e, \varepsilon]$ between both methods, compare cluster, hub, outlier sets. See [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis) for more direction.
4. Plot results - we execute python scripts that read in data outputs from the clustering algorithms and the analysis scripts. See [`visualization`](https://github.com/JoetheManHowie/NUSCAN/tree/main/visualization) for more details.

### Notes

Both NUSCAN and USCAN have the option to output two text files one called `<graphfile>-eta-eps-mu-thres.cluster_nuscan` and `<graphfile>-eta-eps-mu-thres.prob_nuscan` (for uscan the thres is not present and the suffix is "_uscan").
The two files are required to run the code in [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis), as the code assumes the formatting produced by NUSCAN and USCAN. See [`uscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) and [`nuscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) for more information on the files produced, and see [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis) for more information on the analyzes preformed on the files.
