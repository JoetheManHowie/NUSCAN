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
    util.plot_presets()
    path = sys.argv[1]
    df_dict = util.load_all_data_sets(path, ".cluster_compare", util.load_prob_compare_data)
    
    for eta, eps, mu in [(0.5, 0.5, 5), (0.2, 0.5, 2), (0.5, 0.2, 2)]:
        eta_set, eps_set, mu_set = util.get_sub_df(df_dict, eta, eps, mu)
        util.make_time_plot_two(eta_set, eps_set, df_dict.keys(),
                                f"{path}/plots/jac_eta_eps-{eta}-{eps}-{mu}.png",
                                x1="eta", x2="epsilon", ycol="jac", xlab=r"$\eta$ and $\varepsilon$", ylab="", log_flag=False) 
        util.make_time_plot_one(mu_set, df_dict.keys(),
                                f"{path}/plots/jac_mu-{eta}-{eps}-{mu}.png",
                                x="mu", ycol="jac", xlab=r"$\mu$", ylab="Cluster Jaccard similarity", log_flag=False) 
        util.make_time_plot_two(eta_set, eps_set, df_dict.keys(),
                                f"{path}/plots/r_eta_eps-{eta}-{eps}-{mu}-runtime.png",
                                x1="eta", x2="epsilon", ycol="", xlab=r"$\eta$ and $\varepsilon$", ylab="RMSE", log_flag=False) 
        util.make_time_plot_one(mu_set, df_dict.keys(),
                                f"{path}/plots/rmse_mu-{eta}-{eps}-{mu}-runtime.png",
                                x="mu", ycol="rmse", xlab=r"$\mu$", ylab="RMSE", log_flag=False) 
        
        
if __name__=="__main__":
    main()
