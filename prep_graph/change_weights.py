#!/usr/bin/env python3

import sys
import os
import subprocess
import numpy as np
from time import time
from fileinput import FileInput

def main():
    """converts a graph with probability weights to a graph with exponentailly distributed weights, and makes the graph symmetric"""
    beta = 2
    old_file = sys.argv[1]
    new_file = "exp_"+old_file.split(".")[0]+".unsorted"
    os.system("cp "+old_file+" "+new_file)
    length = int(subprocess.check_output("wc -l "+old_file, shell=True).split()[0])//2
    
    with FileInput(new_file, inplace=True) as phil:
        print(length)
        p_vals = [np.random.exponential(beta) for i in range(length)]
        max_p = max(p_vals)
        counter = 0
        for line in phil:
            u,v,p = line.rstrip().split()
            if u>v: continue
            new_p =  p_vals[counter]/max_p####np.exp(-random()*lamb)*lamb/10
            print(u+"\t"+v+"\t"+str(round(new_p, 3)))
            print(v+"\t"+u+"\t"+str(round(new_p, 3)))
            counter +=1
    final_name = new_file.split(".")[0]+".sorted"
    os.system("sort -k1n -k2n "+new_file+" > "+final_name)
    os.system("rm "+new_file)
    

if __name__=="__main__":
    t1 = time()
    main()
    print("Time to Write:", time()-t1)
