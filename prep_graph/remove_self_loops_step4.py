#!/usr/bin/env python3

from time import time
import numpy as np
import sys
import os
from fileinput import FileInput

def main():
    '''removes any edges (u,u,p) from the graph. Note if a node is only connected to itself, then that id has been removed from the graph.'''
    path = sys.argv[1]
    graphname = sys.argv[2]
    edgelist = import_graph(path, graphname)
    us = np.array(list(set(edgelist[:,0])))
    inverse = -1*np.ones(us[-1]+1, dtype=np.int64)
    for i in range(len(us)):
        inverse[us[i]] = i
    save_graph(path+"nsl_"+graphname, edgelist, inverse)


def save_graph(savename, edgelist, inverse):
    os.system("touch "+savename)
    with open(savename, "w") as writer:
        for u,v,p in edgelist:
            pri = str(inverse[u])+"\t"+str(inverse[v])+"\t"+str(p/1000)+"\n"
            writer.write(pri)
            

def import_graph(path, fuel):
    edgelist = []
    with open(path+fuel, 'r') as el:
        for line in el:
            u, v, p = line.rstrip().split()
            u = int(u)
            v = int(v)
            if (u==v): continue
            p = int(float(p)*1000)
            arr = [u,v,p]
            edgelist.append(arr)
    edgelist = np.array(edgelist)
    return edgelist
    

if __name__=="__main__":
    t1 = time()
    main()
    print("Time to complete:", time()-t1)
