import sys
import os


fn = sys.argv[1]
base=fn.split(".")[0]
os.system(f"sort -n -k1,1 -k2,2 {fn} > {fn}.sorted")
