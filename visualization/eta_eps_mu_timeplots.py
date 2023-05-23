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
    sep = "_"
    df_ndict = util.load_all_data_sets(path, ".nuscan")#, util.load_runtime_data_no_thres, sep=sep)
    for eta, eps, mu in [(0.5, 0.5, 5), (0.2, 0.5, 2), (0.5, 0.2, 2)]:
        eta_nset, eps_nset, mu_nset = util.get_sub_df(df_ndict, eta, eps, mu)
        util.make_time_plot_two(eta_nset, eps_nset, df_ndict.keys(),
                                f"{path}/plots/eta_eps-{eta}-{eps}-{mu}-runtime.png",
                                x1="eta", x2="epsilon", ycol="time",
                                xlab=r"$\eta$ and $\varepsilon$", ylab="Time (sec)")

        util.make_time_plot_one(df=mu_nset, graphname=df_ndict.keys(),
                                savename=f"{path}/plots/mu-{eta}-{eps}-{mu}-runtime.png",
                                x="mu", ycol="time", xlab=r"$\mu$", ylab="Time (sec)", log_flag=True)


if __name__=="__main__":
    main()
