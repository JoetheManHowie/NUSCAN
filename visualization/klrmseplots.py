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
    df_dict = util.load_all_data_sets(path, ".prob_compare", util.load_prob_compare_data)
    
    for eta, eps, mu in [(0.5, 0.5, 5), (0.2, 0.5, 2), (0.5, 0.2, 2)]:
        eta_set, eps_set, mu_set = util.get_sub_df(df_dict, eta, eps, mu)
        util.make_time_plot_two(eta_set, eps_set, df_dict.keys(),
                                f"{path}/plots/kl_div_eta_eps-{eta}-{eps}-{mu}-runtime.png",
                                x1="eta", x2="epsilon", ycol="k_l_div", xlab=r"$\eta$ and $\varepsilon$", ylab="K-L Divergence", log_flag=False) 
        util.make_time_plot_one(mu_set, df_dict.keys(),
                                f"{path}/plots/kl_div_mu-{eta}-{eps}-{mu}-runtime.png",
                                x="mu", ycol="rmse", xlab=r"$\mu$", ylab="K-L Divergence", log_flag=False) 
        util.make_time_plot_two(eta_set, eps_set, df_dict.keys(),
                                f"{path}/plots/rmse_eta_eps-{eta}-{eps}-{mu}-runtime.png",
                                x1="eta", x2="epsilon", ycol="rmse", xlab=r"$\eta$ and $\varepsilon$", ylab="RMSE", log_flag=False) 
        util.make_time_plot_one(mu_set, df_dict.keys(),
                                f"{path}/plots/rmse_mu-{eta}-{eps}-{mu}-runtime.png",
                                x="mu", ycol="rmse", xlab=r"$\mu$", ylab="RMSE", log_flag=False) 
        
        
if __name__=="__main__":
    main()
