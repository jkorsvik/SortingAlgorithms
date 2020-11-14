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
from src.subquad_sorting_algorithms import quicksort, mergesort, iterative_quicksort, iterative_quicksort_shufffle
from src.combined_sorting_algorithm import mergesort_combined
from src.standard_sorters import numpy_sort, python_sort

from src.utility import time_sorting_algorithms, ArrayGenerator

if Path('../data').exists():
    data_directory = PurePath("../data")
    print(data_directory)

today = datetime.date.today()
date_str = today.strftime("%d-%b-%Y")
print(date_str)


# N for 2-base generator, 2^N
N = 20
seed = 58
#cols = {"Ascending" : np.single, "Descending" : np.single, "Random" : np.single, "Structured" : np.single, "Integers" :np.int32}

quadratic_algorithms = [bubble_sort, insertion_sort]
subquad_algorithms = [python_sort, numpy_sort, 
iterative_quicksort_shufffle, mergesort, mergesort_combined]

#result_path = f"{data_directory}/subquad_N{N}_seed{seed}_threshquickrandom_{date_str}.csv"
result_path = f"{data_directory}/quadratic_N{N}_seed{seed}_bubble_sort_mod_{date_str}.csv"

df_results = bench_algos(
    quadratic_algorithms, 
    N=N, seed=seed, 
    csv_path_name=result_path)
        



df_results.to_csv(result_path)
