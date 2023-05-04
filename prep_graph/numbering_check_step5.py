#!/usr/bin/env python3

import sys

def main():
    graph = sys.argv[1]
    last_u = -1
    last_v = -1
    
    with open(graph, "r") as openfile:
        for line in openfile:
            u,v,p  = line.rstrip().split()
            u = int(u)
            v = int(v)
            #if last_u == -1 and last_v == -1:
             
            if last_u < u-1:
                print(f"nodes {last_u} to {u} are missing") 
                print(f"goes from edge ({last_u, last_v}) to ({u}, {v})")
                
            last_u = u
            last_v = v
            

if __name__=="__main__":
    main()
