import functools
import time
from copy import copy
from statistics import mean, stdev

from quadratic_sorting_algorithms import insertion_sort, bubble_sort
import numpy as np

def repeating_timer(record, iters=10, *args_, **kwargs_):
    def inner_function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Timing array of {len(kwargs['array'])} elements {iters} times")
            for algorithm in kwargs['function_list']:
                array_copy = copy(kwargs['array'])
                record[algorithm.__name__] = []
                for _ in range(iters):
                    start_time = time.perf_counter()
                    algorithm(array_copy) # Runs algorithm
                    end_time = time.perf_counter()
                    run_time = end_time - start_time
                    record[algorithm.__name__].append(run_time)
                    array_copy = copy(kwargs['array'])
                print("Finished {} in mean {} +-[{}] secs".format(
                    repr(algorithm.__name__), 
                    round(mean(record[algorithm.__name__]), 3),
                    round(stdev(record[algorithm.__name__]), 5)
                ))
        return wrapper
    return inner_function


    
def time_sorting_algorithms(
    functions: list, 
    array: list or np.array, 
    iters: int=10
) -> dict:

    record = dict()

    @repeating_timer(record=record, iters=iters)
    def time_algorithms(function_list: list, array: list or np.array):
        for function in function_list:
            function(copy(array))
    
    time_algorithms(function_list=functions, array=array)

    return record

A = np.random.random(1000)

d = time_sorting_algorithms([insertion_sort, bubble_sort], A)

print(d)




