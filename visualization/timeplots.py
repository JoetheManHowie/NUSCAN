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
    ext =  sys.argv[2]
    tag = ext.split('.')[-1]
    df_dict = util.load_all_data_sets(path, ext)
    for eta, eps, mu in [(0.5, 0.5, 5), (0.2, 0.5, 2), (0.5, 0.2, 2)]:
        eta_set, eps_set, mu_set = util.get_sub_df(df_dict, eta, eps, mu)
        util.make_time_plot_two(eta_set, eps_set, df_dict.keys(), f"{path}/plots/{tag}_eta_eps-{eta}-{eps}-{mu}-runtime.png" )
        util.make_time_plot_one(mu_set, df_dict.keys(), f"{path}/plots/{tag}_mu-{eta}-{eps}-{mu}-runtime.png")

if __name__=="__main__":
    main()
