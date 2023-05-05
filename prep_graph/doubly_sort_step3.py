#!/usr/bin/env python3

import sys
import os


path = sys.argv[1]
fn = sys.argv[2]
base=fn.split(".")[0]
os.system(f"sort -n -k1,1 -k2,2 {path}/{fn} > {path}/{base}.sorted")
