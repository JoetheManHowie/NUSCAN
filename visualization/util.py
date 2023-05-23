#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import os

########################################
### utility functions for dataframes ###
########################################

def df_col_eq_val(df, col, val):
    return df.loc[df[col]==val]

def df_col_to_numpy(df, col):
    return df[col].to_numpy()

def get_sub_df(graphs, eta=0.5, eps=0.5, mu=5):
    mu_set  = {name:graph.loc[graph.eta.eq(eta) & graph.epsilon.eq(eps)] for name, graph in graphs.items()}
    eps_set = {name:graph.loc[graph.eta.eq(eta) & graph.mu.eq(mu)] for name, graph in graphs.items()}
    eta_set = {name:graph.loc[graph.epsilon.eq(eps) & graph.mu.eq(mu)] for name, graph in graphs.items()}
    return eta_set, eps_set, mu_set

######################################
### utility functions for plotting ###
######################################

def make_time_plot_two(df1, df2, graphname, savename, x1="eta", x2="epsilon", ycol="time", xlab=r"$\epsilon$ and $\eta$", ylab="Time (sec)", log_flag=True):
    plt.figure()
    num = 0
    for i in graphname:
        plt.subplot(3,3,1+num)
        plt.plot(df1[i][x1], df1[i][ycol])
        plt.scatter(df1[i][x1], df1[i][ycol])
        plt.plot(df2[i][x2], df2[i][ycol], marker="*")
        plt.scatter(df2[i][x2], df2[i][ycol])
        if log_flag: plt.semilogy()
        yl = list(df1[i][ycol].to_numpy()) + list(df2[i][ycol].to_numpy())

        lab_log_lay_lim(i,xlab,ylab, yl)
        num+=1
    plt.savefig(savename)
    #plt.show()

def make_time_plot_one(df, graphname, savename, x="mu", ycol="time", xlab=r"$\mu$", ylab="Time (sec)", log_flag=True):
    plt.figure()
    num = 0
    for i in graphname:
        plt.subplot(3,3,1+num)
        yl = df[i][ycol]
        plt.plot(df[i][x], yl)
        plt.scatter(df[i][x], yl)
        if log_flag: plt.semilogy()
        lab_log_lay_lim(i,xlab,ylab, yl)
        num+=1
    plt.savefig(savename)
    #plt.show()

def lab_log_lay_lim(i,xlab,ylab, yl):
    if len(yl) > 0:
        fmi, fma = find_mags(yl)
        plt.ylim([fmi, fma])
    plt.title(i)

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.tight_layout()

def find_mags(yl):
    ymin = min(yl)
    ymax = max(yl)
    mi = 0
    ma = 0
    if ymin!=0:
        mi = 10**np.floor(np.log10(ymin))
    if ymax!=0:
        ma = 10**np.ceil(np.log10(ymax))
    if mi==ma:
        if ma==0:
            ma=1
            mi=-1
        elif ma<0:
            ma /=10
            mi *=10
        else:
            ma *=10
            mi /=10
    if mi==0:
        mi==-1
    return (mi, ma)

def plot_presets(ss=8):
    mpl.style.use("seaborn")
    plt.rc('axes', titlesize=ss) #fontsize of the title
    plt.rc('axes', labelsize=ss) #fontsize of the x and y labels
    plt.rc('legend', fontsize=ss*2/3) #fontsize of the legend
    plt.rc('xtick', labelsize=ss)
    plt.rc('ytick', labelsize=ss)


####################
### Loading Data ###
####################

def load_aed_anui_data(filename, path):
    cols1 = ["eta", "epsilon", "mu", "AED", "ANI", "ANI", "ANUI"]
    cols2 = ["eta", "epsilon", "mu", "thres", "AED", "ANI", "ANI", "ANUI"]
    dfn = pd.DataFrame(columns=cols2)
    dfu = pd.DataFrame(columns=cols1)
    with open(f"{path}/{filename}", "r") as fn:
        for line in fn:
            stuff = [float(i) for i in line.split()]
            if len(stuff) == len(cols2):
                dfn = pd.concat([dfn, pd.DataFrame([stuff], columns=cols2)], axis=0, ignore_index=True)
            else:
                dfu = pd.concat([dfu, pd.DataFrame([stuff], columns=cols1)], axis=0, ignore_index=True)

    return (dfn, dfu)

def load_runtime_data(filename, path):
    cols = ["eta", "epsilon", "mu", "time", "cores", "clusters", "hubs", "outliers"]
    if filename.endswith("nuscan"):
        cols=["eta", "epsilon", "mu", "thres", "time", "cores", "clusters", "hubs", "outliers"]
    df = pd.read_csv(f"{path}/{filename}", names=cols, sep="\s+")
    return df

def load_runtime_data_no_thres(filename, path):
    cols = ["eta", "epsilon", "mu", "time", "cores", "clusters", "hubs", "outliers"]
    df = pd.read_csv(f"{path}/{filename}", names=cols, sep="\s+")
    return df

def load_prob_compare_data(filename, path):
    cols = ["eta", "epsilon", "mu", "thres", "edges_included", "k_l_div", 'rmse', "t_ratio", "t_diff", "t_DP", "t_LCLT"]
    df = pd.read_csv(f"{path}/{filename}", names=cols, sep="\s+")
    return df

def load_cluster_compare_data(filename, path):
    cols = ["eta", "epsilon", "mu", "thres", "jac", "unmatched_uc", "unmatched_uv",  "unmatched_nc",  "unmatched_nv", "hubs_r", "outliers_r", "cores_r", "noncores_r"]
    df = pd.read_csv(f"{path}/{filename}", names=cols, sep="\s+")
    return df

def load_all_data_sets(path, ext, funct=load_runtime_data,sep="-"):
    df_dict = dict()
    for filename in os.listdir(path):
        if filename.endswith(ext)==False: continue
        print(filename)
        df_dict[filename.split(sep)[0]] = funct(filename, path)
    return df_dict
