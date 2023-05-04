#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import torch

def main():
    u_file = sys.argv[1]
    n_file = sys.argv[2]
    # extract the t value from nuscan file name
    ttt = int(n_file.split("-")[-1].split(".cluster")[0])+2
    u_data = load_data(u_file)
    n_data = load_data(n_file)

    print(check_clusters(u_data, n_data))


def check_clusters(d1, d2):
    jacc = list(list())
    subs = d2[0]
    
    for c1 in d1[0]:
        ans = 0
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
                break
        jacc.append(ans)

            
    jac = 1
    if len(jacc) !=0:
        jac = np.mean(jacc)
    hub_ratio = 0
    if len(d1[1])==0 and len(d2[1])==0:
        hub_ratio=1
    elif len(d2[1]) == 0:
        hub_ratio=0
    else:
        hub_ratio = len(d1[1])/len(d2[1])
    
    outlier_ratio = 0
    if len(d1[2])==0 and len(d2[2])==0:
        outlier_ratio=1
    elif len(d2[2]) == 0:
        outlier_ratio=0
    else:
        outlier_ratio = len(d1[2])/len(d2[2])

    return jac, hub_ratio, outlier_ratio

    
def load_data(this_file):
    clusters = list()
    hubs = list()
    outliers = list()
    with open(this_file, "r") as mf:
        for line in mf:
            line = line.strip()
            if line.endswith("hub"):
                hubs.append(int(line.split()[0]))
            elif line.endswith("outlier"):
                outliers.append(int(line.split()[0]))
            else:
                clusters.append([int(num) for num in line.split()])
    return clusters, hubs, outliers
    

if __name__=="__main__":
    main()
