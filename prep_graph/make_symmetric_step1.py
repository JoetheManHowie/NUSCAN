#!/usr/bin/env python3

import sys
from fileinput import FileInput
from time import time

def main():
    '''removes self loops and makes symmetric'''
    with FileInput(sys.argv[1], inplace = True) as filename:
        for line in filename:
            u, v, p = line.rstrip().split()
            if u>=v: continue
            print(u+"\t"+v+"\t"+ p)
            print(v+"\t"+u+"\t"+ p)
            
        

if __name__=="__main__":
    t1 = time()
    main()
    print("time to write: ",time()-t1)
