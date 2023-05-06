#!/usr/bin/env python3

import multiprocessing as mp
import subprocess

def run_cpp_script(graph, eta, eps, mu, thres, output):
    base = input_file.split('/')[-1].split('.')[0]
    output_file = f"{base}".out
    subprocess.run([f"./nuscan {input_file} {eta} {eps} {mu} {thres} {output}", input_file, output_file])

if __name__ == "__main__":
    # list of input files to run the script on
    input_files = ["input1.txt", "input2.txt", "input3.txt", "input4.txt", "input5.txt"]
    
    # number of parallel processes to run
    num_processes = 4
    
    # create a pool of processes
    pool = mp.Pool(processes=num_processes)
    
    # apply the `run_cpp_script` function to each input file in parallel
    pool.map(run_cpp_script, input_files)
    
    # close the pool of processes
    pool.close()
