#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore")
## compares differences between DP method and L-CLT computed P[e, epsilon] values and times to compute edges
## ./compare_nuscan_to_uscan.py <path-to-.prob_uscan> <path-to-.prob_nuscan>

def main():
    columns=["u", "v", "prob", "p", "k", "t"]
    #dtye = {"u,":np.float64, "v":np.float64, "prob":np.float64, "p":np.float64, "k":np.float64, "t":np.float64}
    u_file = sys.argv[1]
    n_file = sys.argv[2]
    # extract t from nuscan filename
    path, eta, eps, mu, end = n_file.split("-")
    thres = int(end.split(".")[0])+2
    # import uscan as df
    uscan = pd.read_csv(u_file, sep="\s+",names=columns, on_bad_lines='skip')#, dtype=dtye)
    # import nuscan as df
    nuscan = pd.read_csv(n_file, sep="\s+",names=columns, on_bad_lines='skip')#, dtype=dtye)

    #df['column_name'] = np.isclose(df['column_name'].values, df['column_name'].astype(int).values)

    # merge uscan and nuscan
    combine = pd.merge(uscan,nuscan, on=["u", 'v', 'k'])
    # keep only edges with large enough ku and positive P[e, epsilon]
    clamp = 1e-300
    compare = combine.loc[(combine.k>=thres) & (combine.p_x>clamp) & (combine.p_y>clamp) ]
    #print(compare.sort_values(by=["k", "t_x", "t_y"]))
    # call methods for computing K-L divergence, RMSE, time saved,
    #print(r"Number of edges with non-zero P[e, epsilon] that used Lyapunov CLT = {}".format(len(compare)))
    p_x = compare.p_x.to_numpy()
    p_y = compare.p_y.to_numpy()

    #kl_div = kl_divergence(p_x, p_y)
    Mval = M_val(p_x, p_y)
    jsd = 0.5 * kl_divergence(p_x, Mval) + 0.5 * kl_divergence(p_y, Mval)
    #print(f"K-L divergence = {kl_div:.4f}")

    rmse = RMSE(p_x, p_y)
    # print(f"RMSE = {rmse:.4f}")

    t_x = compare.t_x.to_numpy()
    t_y = compare.t_y.to_numpy()

    tr, ts = time_saved(t_x, t_y)
    #print(f"The time saved by NUSCAN is {ts:.4f} seconds  which is a {tr:.4f}x factor speed up")
    print(eta, eps, mu, thres-2, len(compare), jsd, rmse, tr, ts, t_x.sum(), t_y.sum())

def norm_probs(p):
    '''p is a numpu array'''
    return p/p.sum()

def M_val(p, q):
    # p_norm = norm_probs(p)
    # q_norm = norm_probs(q)
    res_arr = np.array([(pp+qq)/2 for pp, qq in zip(p, q)])#(p_norm, q_norm)])
    return res_arr

def kl_divergence(p, q):
    p_norm = norm_probs(p)
    q_norm = norm_probs(q)
    res_arr = [pp*np.log(pp/qq) for pp, qq in zip(p_norm, q_norm)]
    K_L_div = sum(res_arr)
    return K_L_div

def RMSE(pu, pn):
    if len(pn) == 0: return 0
    return np.sqrt(sum([(p_n - p_u)**2 for p_n, p_u in zip(pn, pu)])/len(pn))

def time_saved(tu, tn):
    tut = tu.sum()
    tnt = tn.sum()
    if tnt == 0:
        if tut==tnt:
            return (1, tut - tnt)
        else:
            return (np.inf, tut - tnt)
    return (tut/tnt, tut - tnt)


if __name__=="__main__":
    main()
