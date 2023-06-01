# Analysis
--------------

In our paper, [*Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem*](https://github.com/JoetheManHowie/NUSCAN/blob/main/Revised_L_CLT_Jaccard_VLDB_FULL_version.pdf) we preformed a series of experiments on different datasets. In this directory we have provided code for reproducing these experiments with some python scripts that read the output files from nuscan and uscan.

## Experiments
----------------

In Section 4 of our paper we outline four different experiments to test the efficiency, scalability, accuracy, and effectiveness of the NUSCAN algorithm. In this directory we have python scripts that generate outputs from the output files of [`uscan`](https://github.com/JoetheManHowie/NUSCAN/tree/main/uscan) and [`nuscan`](https://github.com/JoetheManHowie/NUSCAN/tree/main/nuscan) and the formatted graph file.

### Graph properties

The script [`metrics.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/metrics.py) prints the following information about the graph:

`<number of vertices> <number of edges> <density> <cluster coefficient of deterministic graph> <maximum degree> <average degree>`

and to run the command in the terminal type `./metrics <path to formatted graph>`

### Comparing NUSCAN and USCAN clusterings

We want to know how accurate the clustering of NUSCAN is compared to USCAN.
To globally compare the cluster sets, hubs, outliers, and cores we run the script [`cluster_compare.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/cluster_compare.py) that can be executed in the terminal by passing both .cluster_nuscan and .prob_nuscan (or _uscan) as:

`./cluster_compare.py <path to .cluster_uscan file> <path to .cluster_nuscan file>`

and the program outputs the following results

`<eta> <eps> <mu> <thres> <Average Jaccard similarity between cluster sets> <number of unmatched uscan clusters> <number of vertices in unmatched uscan clusters> <number of unmatched nuscan clusters> <number of vertices in unmatched nuscan clusters> <Jaccard similarity of hubs> <Jaccard similarity of outliers> <Jaccard similarity of cores>`

The Jaccard similarities are computed by iterating over the clusters in USCAN and matching them with clusters in NUSCAN that share at least half the elements of the set, where both the cluster sets are order by largest clusters to smallest.

### Comparing Lyapunov CLT to DP method

We want to compare the two methods of calculating $P[e, \varepsilon]$ to observe the time saved and approximation quality.
To locally compare the quality of the clusters we compare the probabilities $P[e, \varepsilon]$ calculated by both algorithms. Since not every edge passes through these algorithms due to $\eta$ pruning and number of common neighbours, we only compare the edges that pass through the different methods. We can compute K-L Divergence, RMSE, and the time improvements from the .prob_nuscan and .prob_uscan files produced by running the respective algorithms. We can execute the code [`compare_nuscan_to_uscan.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/compare_nuscan_to_uscan.py):

`./compare_nuscan_to_uscan.py <path to .prob_uscan> <path to .prob_nuscan>`

And this prints the following output:

`<eta> <eps> <mu> <thres> <number of edges that past through both methods> <K-L divergence> <RMSE> <ratio of time sums> <difference of times> <sum of DP times> <sum of L-CLT times>`


### Cluster quality metrics

There are two metrics we used to measure the quality of clusters when there is no ground truth. The two metrics were $AED$ and $Q_{ANUI}$ and we run the code [`aed_anui.py`](https://github.com/JoetheManHowie/NUSCAN/blob/main/analysis/aed_anui.py) to calculate both values from the .cluster_nuscan and .prob_nuscan (or _uscan) files.

`./aed_anui.py <path to .cluster_nuscan> <path to .prob_nuscan>`

which prints out:

`<eta> <eps> <mu> <thres> <AED value> <AVI value> <AVU value> <ANUI value>`
