l#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys

# compares cluster results between uscan and nuscan
# ex: ./cluster_compare.py <path-to-.cluster_uscan> <path-to-.cluster_nuscan>

def main():
    u_file = sys.argv[1]
    n_file = sys.argv[2]

    # extract the t value from nuscan file name
    path, eta, eps, mu, end = n_file.split("-")
    thres = end.split(".")[0]
    u_data = load_data(u_file)
    n_data = load_data(n_file)

    #print(get_lengths(u_data))
    #print(get_lengths(n_data))

    jac, umu, umn = check_clusters(u_data[0], n_data[0])
    hub_ratio = ratio(u_data[1], n_data[1])
    outlier_ratio = ratio(u_data[2], n_data[2])
    core_ratio = ratio(u_data[3], n_data[3])
    # ratios are unscan/nuscan
    print(eta, eps, mu, thres, jac, len(umu), count_list(umu), len(umn), count_list(umn), hub_ratio, outlier_ratio, core_ratio)


def count_list(lis):
    return len([len(u) for u in lis])

def sort_lol(lis):
    return sorted(lis, key=lambda x: len(x), reverse=True)

def check_clusters(clus1, clus2):
    sc1 = sort_lol(clus1)
    sc2 = sort_lol(clus2)
    jacc = list(list())
    subs = sc2
    unmatched = list()
    ### gets jaccard simiarlity of closely (>0.5) matching sets of clusters
    for c1 in sc1:
        #print(len(c1))
        ans = 0
        flag = False
        for i in range(len(subs)):
            c2 = subs[i]
            s1 = set(c1)
            s2 = set(c2)
            un = len(s1.union(s2))
            it = len(s1.intersection(s2))

            if un!=0:
                ans = it/un
            if ans > 0.5:
                del subs[i]
                flag = True
                break
        if flag:
            jacc.append(ans)
        else:
            unmatched.append(c1)
    ## unmatched clusters

    ### mean jaccard similarity ###
    jac = 1
    if len(jacc) !=0:
        jac = np.mean(jacc)

    return jac, unmatched, subs

def ratio(x1, x2):
    rat = 0
    if len(x1)==0 and len(x2)==0:
        rat=1
    elif len(x2) == 0:
        rat=0
    else:
        s1 = set(x1)
        s2 = set(x2)
        un = len(s1.union(s2))
        intr = len(s1.intersection(s2))
        rat = intr/un
    return rat

def get_lengths(data):
    return [len(d) for d in data]

def load_data(this_file):

    clusters = list()
    hubs = list()
    outliers = list()
    cores = list()
    spt = "_"
    with open(this_file, "r") as mf:
        for line in mf:
            line = line.rstrip()
            #print(line)
            if line.endswith("_h"):
                hubs.append(int(line.split(spt)[0]))
            elif line.endswith("_o"):
                outliers.append(int(line.split(spt)[0]))
            else:
                cores.extend([int(num.split(spt)[0]) for num in line.split() if num.split(spt)[1]=="c"])
                clusters.append([int(num.split(spt)[0]) for num in line.split()])

    return clusters, hubs, outliers, cores



if __name__=="__main__":
    main()
