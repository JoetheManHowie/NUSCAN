#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import torch
import itertools

def main():
    ffile = sys.argv[1]
    # extract the t value from nuscan file name
    clusters = load_clusters(ffile)
    graph = 0


def AED(G, C):
    total_expected_density = 0
    total_clusters = 0
    for cluster in C:
        cluster_expected_density = 0
        for i, j in itertools.combinations(cluster, 2):
            if (i, j) in G:
                prob = G[(i, j)]
            elif (j, i) in G:
                prob = G[(j, i)]
            else:
                continue
            cluster_expected_density += prob
        total_expected_density += cluster_expected_density / (len(cluster) * (len(cluster) - 1) / 2)
        total_clusters += 1
    return total_expected_density / total_clusters

    

def load_clusters(this_file):
    clusters = list()
    with open(this_file, "r") as mf:
        for line in mf:
            line = line.strip()
            if line.endswith("hub") or line.endswith("outlier"):
                continue
            else:
                clusters.append([int(num) for num in line.split()])
    return clusters
    

if __name__=="__main__":
    main()
