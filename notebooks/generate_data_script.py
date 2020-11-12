from bench_algo import bench_algos
import numpy as np
import pandas as pd
import seaborn as sns
import datetime


import os
import sys
from pathlib import Path, PurePath
sys.path.append("..")
# For quicksort
sys.setrecursionlimit(int(1e7))

from src.linear_sorting_algorithms import radixsort
from src.quadratic_sorting_algorithms import bubble_sort, insertion_sort
from src.subquad_sorting_algorithms import quicksort, mergesort, iterative_quicksort
from src.combined_sorting_algorithm import mergesort_combined

from src.utility import time_sorting_algorithms, ArrayGenerator

if Path('../data').exists():
    data_directory = PurePath("../data")
    print(data_directory)


# N for 2-base generator, N^2
N = 14
cols = {"Ascending" : np.single, "Descending" : np.single, "Random" : np.single, "Structured" : np.single, "Integers" :np.int32}

quadratic_algorithms = [bubble_sort, insertion_sort]
subquad_algorithms = [iterative_quicksort, mergesort, mergesort_combined]


df_results = bench_algos(subquad_algorithms, N=22)
        
today = datetime.date.today()
date_str = today.strftime("%d-%b-%Y")


df_results.to_csv(f"{data_directory}/benchmark_results_test{date_str}.csv")
