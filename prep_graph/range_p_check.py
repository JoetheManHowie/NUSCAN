#!/usr/bin/env python3

import sys

def main():
    '''checks that a graph is only contains values between 0 and 1'''
    graph = sys.argv[1]


    with open(graph, "r") as openfile:
        for line in openfile:
            u,v,p  = line.rstrip().split()
            int_u = int(u)
            int_v = int(v)
            count=0
            if p==0 or p==1:
                print(u,v,p)
                count+=1
        print(f"there are {count} p=0 or p=1 edges.")

if __name__=="__main__":
    main()
