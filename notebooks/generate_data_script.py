import numpy as np
import pandas as pd
import seaborn as sns

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

array_gen = ArrayGenerator(seed=12)

# N for 2-base generator, N^2
N = 14
cols = {"Ascending" : np.single, "Descending" : np.single, "Random" : np.single, "Structured" : np.single, "Integers" :np.int32}

test_data = dict()

for i in range(1, N+1):
    data = np.array([array_gen.sorted_array(i),
            array_gen.reversed_array(i),
            array_gen.random_array(i),
            array_gen.structured_array(i),
            array_gen.integer_array(i)
           ])
    test_data[i] = pd.DataFrame(columns=cols.keys(), data=data.T).astype(cols)

list_of_algorithms = [bubble_sort, insertion_sort, iterative_quicksort, mergesort, mergesort_combined]


df_results = pd.DataFrame(columns=["Algorithm", "2^N", "TypeArray", "Time"])

for N, Array in test_data.items():
    for TypeArray in cols.keys():
        
        for algorithm, times in time_sorting_algorithms(
            functions=list_of_algorithms, 
            array=Array[TypeArray].to_numpy(), 
            iters=5, 
            verbose=True
        ).items():
            
            for time in times:
                
                df_results = df_results.append(
                    {
                    "Algorithm": algorithm, "2^N": N, "TypeArray": TypeArray, "Time": time
                    }, 
                    ignore_index=True
                )
        

df_results.to_csv(f"{data_directory}/benchmark_results_test.csv")
