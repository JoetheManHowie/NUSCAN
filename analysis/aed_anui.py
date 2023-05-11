#!/usr/bin/env python3
from time import time
import numpy as np
import pandas as pd
import sys
import itertools
# for nuscan files
# ex: ./aed_anui.py <path-to-*.cluster_nuscan> <path-to-*.prob_nuscan>
# or for uscan files 
# ex: ./aed_anui.py <path-to-*.cluster_uscan> <path-to-*.prob_uscan> 

def main(debug=False):
    # get text files from command line
    ffile = sys.argv[1]
    efile = sys.argv[2]
    file_name = ffile.split("-")
    thres = ""
    if len(file_name) > 4:
        path, eta, eps, mu, end = file_name
        thres = end.split(".")[0]
    elif len(file_name) == 4:
        path, eta, eps, mu_end = file_name
        mu = mu_end.split(".")[0]

    #suffix = ftype.split("_")[1]
        
    # get list of clusters
    # and u<v edgelist with post clustering data
    t1 = time()
    clusters = load_clusters(ffile)
    graph = load_edges(efile)
    if debug: print(f"Load data {time()-t1:.4f} seconds")
    #adj_list = get_adj_list(graph)
    t1 = time()
    aed = AED(graph, clusters)
    #print(f"AED = {aed:.4f}")
    if debug: print(f"AED: Computed in {time()-t1:.4f} seconds")
    t1 = time()
    q_avi, q_avu, q_anui = calculate_anui(clusters, graph)
    if debug: print(f"Q_anui: Computed in {time()-t1:.4f} seconds")

    print(eta, eps, mu, thres, aed, q_avi, q_avu, q_anui)
    #print(calculate_unifiability(clusters[0],clusters[1], graph))
    #print(calculate_isolatability(clusters[0], graph))
    #print(f"Q_AVI = {q_avi:.4f}")
    #print(f"Q_AVU = {q_avu:.4f}")    
    #print(f"Q_ANUI = {q_anui:.4f}")
    

def calculate_isolatability(Ci, G):
    denominator = sum([G.loc[G.u==i].prob.to_numpy().sum() for i in Ci])
    numerator = sum([float(G.prob.loc[(G.u==i)&(G.v==j)])  for i, j in itertools.combinations(Ci, 2) if i<j and len(G.loc[(G.u==i)&(G.v==j)])==1])
    #print(numerator, denominator)
    if denominator == 0:
        return 0
    return numerator / denominator

def calculate_unifiability(cluster1, cluster2, graph):
    c1 = set(cluster1)
    c2 = set(cluster2)
    union = c2.union(c1)

    c_sort = sorted(list(union))
    numerator = 0
    denominator = 0
    
    for i in c_sort:
        for _, row in graph.loc[graph.u==i].iterrows():
            u = row.u
            v = row.v
            prob = row.prob
            if u in cluster1 and v in cluster2:
                numerator += prob
                
            if (u in cluster1 and v not in cluster1) or ( u not in cluster2 and v in cluster2):
                denominator += prob 
    
    if (denominator - numerator) == 0:
        return 0
    return numerator / (denominator - numerator)


def calculate_anui(clusters, graph):
    avi = 0
    avu = 0
    if len(clusters) > 0:
        avi = sum(calculate_isolatability(cluster, graph) for cluster in clusters) / len(clusters)
        avu = sum(calculate_unifiability(cluster1, cluster2, graph) for cluster1, cluster2 in itertools.combinations(clusters, 2)) / len(list(itertools.combinations(clusters, 2)))
    anui = 0
    if avu == 0:
        anui = avi
    anui = avi / (1 + avi * avu)
    return avi, avu, anui
    

def AED(G, C):
    total_expected_density = 0
    #total_clusters = 0
    if len(C) == 0:
        return 0
    for cluster in C:
        if (len(cluster) - 1) <1:continue
        cluster_expected_density = 0
        for i, j in itertools.combinations(cluster, 2):
            if i>j: continue
            ed = G.loc[(G.u==i)&(G.v==j)]
            if len(ed) == 1:
                cluster_expected_density += float(ed.prob)
        total_expected_density += 2*cluster_expected_density / (len(cluster) * (len(cluster) - 1))
    return total_expected_density / len(C)

    
def load_clusters(this_file):
    clusters = list()
    with open(this_file, "r") as mf:
        for line in mf:
            line = line.strip()
            if line.endswith("_h") or line.endswith("_o"):
                continue
            else:
                clusters.append([int(num.split("_")[0]) for num in line.split()])
    return clusters

def load_edges(csv_file):
    columns=["u", "v", "prob", "p", "k", "t"]
    df = pd.read_csv(csv_file, sep="\s+",names=columns)
    return df
    

if __name__=="__main__":
    main()

'''
    numerator=0
    for i,j in itertools.combinations(Ci, 2):
        if i<j and len(G.loc[(G.u==i)&(G.v==j)])==1:
            float(G.prob.loc[(G.u==i)&(G.v==j)]) 
            #print(float(G.prob.loc[(G.u==i)&(G.v==j)]))
    

    denominator = 0
    for i in Ci:
        print(G.loc[G.u==i].prob.to_numpy())
    
    
    for (u, v), prob in graph.items():
        if u in cluster and v in cluster:
            numerator += prob
        if u in cluster or v in cluster:
            denominator += prob
'''
