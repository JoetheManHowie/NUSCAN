#!/usr/bin/env python3

#ex: ./compareplots.py <path to -full.nuscan files>

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
    df_ndict = util.load_all_data_sets(path, ".nuscan")
    df_udict = util.load_all_data_sets(path, ".uscan")
    for eta, eps, mu in [(0.5, 0.5, 5), (0.2, 0.5, 2), (0.5, 0.2, 2)]:
        eta_nset, eps_nset, mu_nset = util.get_sub_df(df_ndict, eta, eps, mu)
        eta_uset, eps_uset, mu_uset = util.get_sub_df(df_udict, eta, eps, mu)
        
        util.make_time_plot_two(eta_nset, eta_uset, df_ndict.keys(),
                                f"{path}/plots/compare_eta-{eta}-{eps}-{mu}-runtime.png",
                                x1="eta", x2="eta", ycol="time",
                                xlab=r"$\eta$", ylab="Time (sec)")
        util.make_time_plot_two(eps_nset, eps_uset, df_ndict.keys(),
                                f"{path}/plots/compare_eps-{eta}-{eps}-{mu}-runtime.png",
                                x1="epsilon", x2="epsilon", ycol="time",
                                xlab=r"$\varepsilon$", ylab="Time (sec)")
        util.make_time_plot_two(mu_nset, mu_uset, df_ndict.keys(),
                                f"{path}/plots/compare_mu-{eta}-{eps}-{mu}-runtime.png",
                                x1="mu", x2="mu", ycol="time",
                                xlab=r"$\mu$", ylab="Time (sec)")
    
    
if __name__=="__main__":
    main()
