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
    

def load_data(this_file):
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
