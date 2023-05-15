#!/usr/bin/env python3

#ex: ./alter_weights_step0.py <path> <graph>
import os
import sys
import numpy as np
from time import time
from fileinput import FileInput

def main():
    path = sys.argv[1]
    filen = sys.argv[2]
    base = filen.split(".")[0]
    choice = sys.argv[3]
    ext = ''
    if choice =="normal":
        ext = ".ntemp"
    elif choice == "uniform":
        ext = "uniform"
    distro = pick_distribution(choice)
    new_file = path+"/"+base+ext
    os.system(f"cp {path}/{filen} {new_file}")
    with FileInput(new_file, inplace=True) as filename:
        for line in filename:
            edge = line.rstrip().split()
            u = edge[0]
            v = edge[1]
            if u>=v: continue
            p = clamp(distro())
            print(u+"\t"+v+"\t"+ str(round(p, 3)))
            print(v+"\t"+u+"\t"+ str(round(p, 3)))
    new_final = path+"/"+base+"."+choice
    os.system("sort -k1n -k2n "+new_file+" > "+new_final)
    os.system(f"rm {new_file}")
    
def clamp(x):
    if x>=1: return 0.999
    elif x<=0: return 0.001
    else: return x
            
def uniform():
    return np.random.rand(1)[0]

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
        return -1
        

if __name__=="__main__":
    t1 = time()
    main()
    print("time to write: ",time()-t1)
