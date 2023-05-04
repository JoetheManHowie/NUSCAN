#!/usr/bin/env python3

## ./prob_compare.py <uscan_prob_file> <nuscan_prob_file>

import numpy as np
import pandas as pd
import sys

def main():
    columns=["u", "v", "p", "k", "t"]
    u_file = sys.argv[1]
    n_file = sys.argv[2]
    # extract t from nuscan filename
    ttt = int(n_file.split("-")[-1].split(".prob")[0])+2 

    # import uscan as df
    uscan = pd.read_csv(u_file, sep="\s+",names=columns)
    # import nuscan as df
    nuscan = pd.read_csv(n_file, sep="\s+",names=columns)
    # merge uscan and nuscan
    combine = pd.merge(uscan,nuscan, on=["u", 'v', 'k'])
    # keep only edges with large enough ku
    compare = combine.loc[combine.k>=ttt]
    # probabilities as computed by both methods
    pu = compare.p_x.to_numpy()
    pn = compare.p_y.to_numpy()
    clamp = 1e-32
    res_arr = [pi*np.log(pi/pa) for pi, pa in zip(pn, pu) if pa>clamp and pi>clamp]
    '''
    res_arr = list()
    for pi, pa in zip(pn, pu):
        if pa!=0 and pi!=0:
            ans = pi*np.log(pi/pa)
            if ans > 10:
                print(ans, pi, pa)
            res_arr.append(ans)
    '''
    result = sum(res_arr)

    print(len(res_arr), result)


if __name__=="__main__":
    main()
