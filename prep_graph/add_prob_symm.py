#!/usr/bin/env python3

import sys
from fileinput import FileInput
from random import random
from time import time

def main():
    '''adds uniformly random weight to an unweighted graph, and makes it symmetry.'''
    with FileInput(sys.argv[1], inplace = True, backup = '.bak') as filename:
        for line in filename:
            u, v = line.rstrip().split()
            if u==v: continue
            p = random()
            print(u+"\t"+v+"\t"+ str(round(p, 3)))
            print(v+"\t"+u+"\t"+ str(round(p, 3)))
            
        

if __name__=="__main__":
    t1 = time()
    main()
    print("time to write: ",time()-t1)
