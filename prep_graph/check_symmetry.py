#!/usr/bin/env python3

import sys

def main():
    '''checks that a graph is symmetrical (ie (u,v,p) and (v,u,p) exist, note probabilities must be the same)'''
    graph = sys.argv[1]
    stack = {}
    print("BEG: stack size = "+str(len(stack)))
    with open(graph, "r") as openfile:
        for line in openfile:
            u,v,p  = line.rstrip().split()
            int_u = int(u)
            int_v = int(v)
            key = ''
            if (u>v):
                key = v+','+u
            else:
                key = u+','+v
            try:
                val = stack[key]
                if (val == p):
                    del stack[key]
                else:
                    print("prob miss match on u,v = "+key+" with probs = "+p+" and "+val)
            except (KeyError):
                stack[key] = p

    print("stack size = "+str(len(stack)))
    

if __name__=="__main__":
    main()
