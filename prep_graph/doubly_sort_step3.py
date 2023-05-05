#!/usr/bin/env python3

import sys
import os


pathfile = sys.argv[1]
pathl = pathfile.split("/")
fn = pathl[-1] #sys.argv[2]
path = '/'.join(pathl[:-1])
base=fn.split(".")[0]
os.system(f"sort -n -k1,1 -k2,2 {path}/{fn} > {path}/{base}.sorted")
