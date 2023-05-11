#!/usr/bin/env python3

#ex: ./timeplots.py <path to -full.nuscan file>
import util 
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def main():
    #df_set =
    path = sys.argv[1]
    ext =  sys.argv[2]
    df_set = load_all_data_sets(path, ext)
    make_time_plot(df_set)

def make_time_plot(df_set):
    ## plot presets
    ss = 8
    mpl.style.use("seaborn")
    plt.rc('axes', titlesize=ss) #fontsize of the title
    plt.rc('axes', labelsize=ss) #fontsize of the x and y labels
    plt.rc('legend', fontsize=ss*2/3) #fontsize of the legend
    plt.rc('xtick', labelsize=ss) 
    plt.rc('ytick', labelsize=ss)
    for i in range(len(df_set)):
        plt.subplot(3,3,1+i)
        
    

def load_all_data_sets(path, ext):
    df_set = []
    for filename in os.listdir(path):
        if filename.endswith(ext)==False: continue
        print(filename)
        df_set.append(load_runtime_data(filename, path))

def load_runtime_data(filename, path):
    cols = ["eta", "epsilon", "mu", "times", "cores", "clusters", "hubs", "outliers"]
    if filename.endswith(".nuscan"):
        cols=["eta", "epsilon", "mu", "thres", "times", "cores", "clusters", "hubs", "outliers"]
    df = pd.read_csv(f"{path}/{filename}", names=cols, sep="\s+")
    return df
    

if __name__=="__main__":
    main()
