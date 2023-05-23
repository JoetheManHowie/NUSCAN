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
    sep = "-"
    df_dicts = util.load_all_data_sets(path, ".aed_anui", util.load_aed_anui_data, sep=sep)
    df_ndict = {}
    df_udict = {}
    for k,v in df_dicts.items():
        df_ndict[k] = v[0]
        df_udict[k] = v[1]
    eta = 0.5
    eps = 0.5
    mu = 5

    plots(df_ndict, eta, eps, mu, path, "nuscan")
    plots(df_udict, eta, eps, mu, path, "uscan")


def plots(df, eta, eps, mu, path, label):
    eta_set, eps_set, mu_set = util.get_sub_df(df, eta, eps, mu)

    util.make_time_plot_two(eta_set, eps_set, df.keys(),
                            f"{path}/plots/aed_eta_eps-{eta}-{eps}-{mu}-aed-{label}.png",
                            x1="eta", x2="epsilon", ycol="AED",
                            xlab=r"$\eta$ and $\varepsilon$", ylab="AED", log_flag=False)

    util.make_time_plot_one(mu_set, df.keys(),
                            f"{path}/plots/aed_mu-{eta}-{eps}-{mu}-aed-{label}.png",
                            x="mu", ycol="AED",
                            xlab=r"$\mu$", ylab="AED", log_flag=False)
    util.make_time_plot_two(eta_set, eps_set, df.keys(),
                            f"{path}/plots/anui_eta_eps-{eta}-{eps}-{mu}-aed-{label}.png",
                            x1="eta", x2="epsilon", ycol="ANUI",
                            xlab=r"$\eta$ and $\varepsilon$", ylab=r"$Q_{ANUI}$", log_flag=False)

    util.make_time_plot_one(mu_set, df.keys(),
                            f"{path}/plots/anui_mu-{eta}-{eps}-{mu}-aed-{label}.png",
                            x="mu", ycol="ANUI",
                            xlab=r"$\mu$", ylab=r"$Q_{ANUI}$", log_flag=False)


if __name__=="__main__":
    main()
