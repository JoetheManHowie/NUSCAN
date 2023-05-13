#!/usr/bin/env python3

#ex: ./alter_weights_v2_step0.py <path> <graph>

# difference between this and version 1, n files are created and destroyed, instead we have a temp graph, where the edges are weighted prior and scarificed for the new distribution. This was main for execution on compute canada.
import os
import sys
import numpy as np
import random
from time import time

def main():
    path = sys.argv[1]
    filen = sys.argv[2]
    filep = f"{path}/{filen}"
    choice = sys.argv[3]
    distro = pick_distribution(choice)
    with open(filep, "r") as filename:
        for line in filename:
            edge = line.rstrip().split()
            u = edge[0]
            v = edge[1]
            if u>=v: continue
            p = clamp(distro())
            print(u+"\t"+v+"\t"+ str(round(p, 3)))
            print(v+"\t"+u+"\t"+ str(round(p, 3)))
    
    
    
def clamp(x):
    if x>=1: return 0.999
    elif x<=0: return 0.001
    else: return x
            
def uniform():
    return random.uniform(0, 1)
    #return np.random.rand(1)[0]

def normal():
    return np.random.normal(loc=0.5, scale=0.1)

def exponential():
    return np.random.exponential(beta=2)
    

def pick_distribution(choice ):
    if choice == "uniform":
        return uniform
    elif choice == "normal":
        return normal
    elif choice == "exp":
        return exponential
    else:
        return fiftyfifty
        

if __name__=="__main__":
    t1 = time()
    main()
    print("time to write: ",time()-t1)
