#!/usr/bin/env python3

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def main():
    #df_set = 
    df = load_runtime_data()
    

def load_runtime_data():
    filename = sys.argv[1]
    cols = ["eta", "epsilon", "mu", "times", "cores", "clusters", "hubs", "outliers"]
    if filename.endswith(".nuscan"):
        cols=["eta", "epsilon", "mu", "thres", "times", "cores", "clusters", "hubs", "outliers"]
    df = pd.read_csv(filename, names=cols, sep="\s+")
    #print(df)
    return df
    

if __name__=="__main__":
    main()
