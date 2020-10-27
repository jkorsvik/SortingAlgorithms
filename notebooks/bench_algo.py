import numpy as np
import pandas as pd
import seaborn as sns

import os
import sys
from pathlib import Path, PurePath
sys.path.append("..")


# For quicksort
sys.setrecursionlimit(int(1e6))

from src.utility import time_sorting_algorithms, ArrayGenerator


def bench_algos(list_of_algorithms: list, N, seed=42):
    if type(list_of_algorithms) != list:
        list_of_algorithms = list(list_of_algorithms)
    array_gen = ArrayGenerator(seed=seed)

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


    df = pd.DataFrame(columns=["Algorithm", "2^N", "TypeArray", "Time"])

    for N, Array in test_data.items():
        for TypeArray in cols.keys():
            time_and_unpack_to_df(df, list_of_algorithms, N, Array, TypeArray)



def time_and_unpack_to_df(df: pd.DataFrame, 
    list_of_algorithms: list,
    N: int,
    Array: np.array or list,
    TypeArray: str
):
    for algorithm, times in time_sorting_algorithms(
                functions=list_of_algorithms, 
                array=Array[TypeArray].to_numpy(), 
                iters=5, 
                verbose=True
            ).items():
                
                for time in times:
                    
                    df = df.append(
                        {
                        "Algorithm": algorithm, "2^N: N, "TypeArray": TypeArray, "Time": time
                        }, 
                        ignore_index=True
                    )