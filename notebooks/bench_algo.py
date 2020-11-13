import numpy as np
import pandas as pd
import seaborn as sns
import time

import os
import sys
from pathlib import Path, PurePath
sys.path.append("..")


# For quicksort
sys.setrecursionlimit(int(1e6))

from src.utility import time_sorting_algorithms, ArrayGenerator
from src.quadratic_sorting_algorithms import bubble_sort, insertion_sort


def bench_algos(list_of_algorithms: list,
    N, 
    seed=12, 
    cols={
        "Ascending" : np.single, 
        "Descending" : np.single, 
        "Random" : np.single, 
        "Structured" : np.single, 
        "Integers" :np.int32
        },
    csv_path_name=None
    
) -> pd.DataFrame:

    if type(list_of_algorithms) != list:
        list_of_algorithms = list(list_of_algorithms)
    array_gen = ArrayGenerator(seed=seed)

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
            
            df = time_and_unpack_to_df(
                df, 
                list_of_algorithms, 
                N, 
                Array, 
                TypeArray
                )

            toc = time.perf_counter()
            if csv_path_name is not None:
                tic = time.perf_counter()
                if toc - tic > 60*10:
                    df.to_csv(csv_path_name)
    return df

def time_and_unpack_to_df(df: pd.DataFrame, 
    list_of_algorithms: list,
    N: int,
    Array: np.array or list,
    TypeArray: str
) -> pd.DataFrame:

    for algorithm, times in time_sorting_algorithms(
                functions=list_of_algorithms, 
                array=Array[TypeArray].to_numpy(), 
                iters=5, 
                verbose=True
            ).items():
                
                for time in times:
                    
                    df = df.append(
                        {
                        "Algorithm": algorithm, "2^N": N, "TypeArray": TypeArray, "Time": time
                        }, 
                        ignore_index=True
                    )

    return df

if __name__ == "__main__":
    # Test of functionality
    quadratic_algorithms = [bubble_sort, insertion_sort]
    df_res = bench_algos(quadratic_algorithms, N=8)
    print(df_res.head(), df_res.tail())

    
    