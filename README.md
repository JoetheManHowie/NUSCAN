# Introduction
--------------------

This repository contains all the code and instructions neccessary to reproduce the experimental results from our paper "Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem".


## Overview
------------

There are five directories each with their our purpose:

1. [`prep_graphs/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/prep_graph) contains all the python code used to format datasets for the clustering algorithms NUSCAN and USCAN.
3. [`uscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) holds the C++ implementation of USCAN as coded by the authors, with few additions needed for our analysis.
4. [`nuscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) holds the modified USCAN code that includes the NUSCAN algorithm.
5. [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis) has the scripts used to analyze the clusters and probability calculations made by both algorithms.

In each of these directory there are more specific instructions for using the code inside.


## Workflow
--------------

In general to execute the analysis that was done in our paper the following sets must take place:

1. Format graph - NUSCAN and USCAN both operate on undirected probabilistic graphs. See [`prep_graphs/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/prep_graph) for more information on the formatting requirements.
2. Run the graph through both clustering algorithms with the output option to generate the txt files with the probabilities $P[e, \varepsilon]$ for each e and another txt file with the cluster sets, hubs, and outliers. See [`uscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) and [`nuscan/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) for more details.
3. Analyze results - there are some scripts that compute cluster quality, compare $P[e, \varepsilon]$ between both methods, compare cluster, hub, outlier sets. See [`analysis/`](https://github.com/JoetheManHowie/NUSCAN/tree/main/analysis) for more direction.



