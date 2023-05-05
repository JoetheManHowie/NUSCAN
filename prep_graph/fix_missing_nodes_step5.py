#!/usr/bin/env python3

import numpy as np
import sys
import pickle

def main():
    pathfile = sys.argv[1]
    pathl = pathfile.split("/")
    inname = pathl[-1] 
    path = '/'.join(pathl[:-1])
    save_map_flag = False
    if len(sys.argv) > 3:
        unknown = bool(sys.argv[3])
        if unknown == True:
            save_map_flag = True        

    base = inname.split(".")[0]
    savefile = f"{path}/{base}.renumered"
    edgelist, missing = import_graph(path, inname)
    new_edgelist, vm = make_new_graph(edgelist, missing)
    save_graph(new_edgelist, savefile)
    if save_map_flag:
        nom = f"{path}/{base}.pickle"
        save_vertex_map(vm, nom)

    
def save_graph(new_edgelist, savefile):
    with open(savefile, "w") as f:
        for u, v, p in new_edgelist:
            f.write(f"{u} {v} {p/1000:.3f}\n")


def make_new_graph(edgelist, missing):
    # Determine the current highest vertex number
    max_vertex = max(max(edge) for edge in edgelist)

    # Create a mapping of old vertex numbers to new vertex numbers
    vertex_map = dict()
    count = 0
    ## this can be slow for large graphs, improvements are welcome
    for old in range(max_vertex+1):
        if old in missing:
            continue
        vertex_map[old] = count
        count+=1    
    # Create the new edgelist with updated vertex numbers
    new_edgelist = [ (vertex_map[u], vertex_map[v], p) for u, v, p in edgelist]
    return new_edgelist, vertex_map


def save_vertex_map(vm, saveloc):
    print(saveloc)
    vm_file = open(saveloc, 'wb')
    pickle.dump(vm, vm_file)
    vm_file.close()


def import_graph(path, base):
    edgelist = []
    missing = []
    with open(f"{path}/{base}", "r") as el:
        nodes = set()
        for line in el:
            u, v, p = line.rstrip().split()
            u = int(u)
            v = int(v)
            p = int(float(p)*1000)
            nodes.add(u)
            arr = [u,v,p]
            edgelist.append(arr)
        missing = sorted(list(set(range(max(nodes))).difference(nodes)))
    edgelist = np.array(edgelist)
    missing = np.array(missing)
    return edgelist, missing


if __name__=="__main__":
    main()
