#!/usr/bin/env python3
import sys
import numpy as np
from time import time
import multiprocessing
from itertools import combinations
from functools import partial
# for formatted graph file (pre-cluster)
# ex: ./metrics.py <path-to-graph-file>

def main():
    filename = sys.argv[1]
    edges = load_data(filename)
    num_v = max(max(edges))+1
    num_e = len(edges)//2
    adj_list = get_adj_list(edges)
    t1=time()
    cluster_coefficient = calculate_cluster_coefficient_slow(adj_list)
    print(f"time for single thread: {time()-t1:.4f}")
    t1 = time()
    cluster_coefficientt = calculate_cluster_coefficient(adj_list)
    print(f"time for parallel: {time()-t1:.4f}")
    if cluster_coefficient != cluster_coefficientt:
        print("Huston, we have a problem.")
        print(cluster_coefficientt, cluster_coefficient)

    max_degree, ave_degree = count_degrees(adj_list)
    density = 2*num_e/(num_v*(num_v-1))
    '''
    print(f"Cluster coefficient: {cluster_coefficient}")
    print(f"Average degree: {ave_degree}")
    print(f"Maximun degree: {max_degree}")
    '''
    print(num_v, num_e, density, cluster_coefficient, max_degree, ave_degree)

def load_data(filename):
    # read in graph as an edgelist from command line
    with open(filename, 'r') as f:
        edges = [tuple(map(int, line.strip().split()[:-1])) for line in f]
    return edges

def get_adj_list(edges):
    # create adjacency list
    adj_list = {}
    for u, v in edges:
        if u >v: continue
        if u not in adj_list:
            adj_list[u] = set()
        if v not in adj_list:
            adj_list[v] = set()
        adj_list[u].add(v)
        adj_list[v].add(u)
    return adj_list


def calculate_triangles(adj_list, node):
    neighbors = adj_list[node]
    triangles = 0
    for u in neighbors:
        for v in neighbors:
            if u != v and v in adj_list[u]:
                triangles += 1
    return triangles


def calculate_cluster_coefficient(adj_list):
    total_triangles = 0
    total_connected_triples = 0
    pool = multiprocessing.Pool()

    # Calculate triangles for each node in parallel
    triangle_counts = pool.starmap(calculate_triangles, [(adj_list, node) for node in adj_list])
    #print(triangle_counts)
    for node, neighbors in adj_list.items():
        k = len(neighbors)
        if k < 2:
            continue
        connected_triples = k * (k - 1) // 2   # Adjusted calculation

        triangles = triangle_counts[node]

        total_triangles += triangles
        total_connected_triples += connected_triples

    pool.close()
    pool.join()

    if total_connected_triples == 0:
        cluster_coefficient = 0
    else:
        cluster_coefficient = total_triangles / total_connected_triples

    return cluster_coefficient


def calculate_cluster_coefficient_slow(adj_list):
    # calculate cluster coefficient for each node
    total_triangles = 0
    total_connected_triples = 0
    for node in adj_list:
        neighbors = adj_list[node]
        k = len(neighbors)
        if k < 2:
            continue
        # calculate number of triangles and connected triples for this node
        triangles = 0
        connected_triples = k*(k-1)//2
        for u in neighbors:
            for v in neighbors:
                if u != v and v in adj_list[u]:
                    triangles += 1
        # update totals
        total_triangles += triangles
        total_connected_triples += connected_triples

    # calculate cluster coefficient
    if total_connected_triples == 0:
        cluster_coefficient = 0
    else:
        cluster_coefficient = total_triangles / total_connected_triples

    return cluster_coefficient

def count_degrees(adj_list):
    degrees = []
    d_max = 0
    for values in adj_list.values():
        curr_d = len(values)
        if curr_d > d_max:
            d_max = curr_d
        degrees.append(curr_d)
    return d_max, np.mean(degrees)



if __name__=="__main__":
    main()
