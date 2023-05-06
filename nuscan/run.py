#!/usr/bin/env python3

import sys
import os

#graphs = ["CARoad", "core", "DBLP", "douban", "Flickr"]
suffix = ".sorted"
preffix = "../datasets/"

thres = 100 
floats = (0.2, 0.5)
ints = (3, 5)

#for graph in graphs:
graph = sys.argv[1]
path = f"{preffix}/{graph}/{graph}{suffix}"
print(path)
for eta in floats:
    for eps in floats:
        for mu in ints:
            os.system(f"./nuscan {path} {eta} {eps} {mu} {thres} output")
