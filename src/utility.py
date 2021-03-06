import functools
import time
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
from statistics import mean, stdev



def repeating_timer(record, iters, verbose, *args_, **kwargs_):
    def inner_function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if verbose:
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
                    
                if verbose:    
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
    iters: int=10,
    verbose: bool=False
) -> dict:

    record = dict()

    @repeating_timer(record=record, iters=iters, verbose=verbose)
    def time_algorithms(function_list: list, array: list or np.array):
        for function in function_list:
            function(copy(array))
    
    time_algorithms(function_list=functions, array=array)

    return record


class ArrayGenerator():
    """
    Generatorclass for creating arrays of 2^n size. Useful for
    analazing log of 2 algorithms as we of have given compute problems
    """    

    def __init__(
        self,
        seed: int=None
    ):
        """
        Set seed for numpy RNG 
        """
        self.seed = seed
        self.rng = np.random.default_rng(seed=seed)

    def sorted_array(self, n):

        return np.arange(0, int(2**n)).astype('int32')

    def reversed_array(self, n):
        return np.arange(int(2**n), 0, -1).astype('int32')
    
    def random_array(self, n):
        return self.rng.random(int(2**n)).astype('float32')

    def structured_array(self, n):
        """
        Creates an array with an obvious structure, already ascending.
        """
        array = np.arange(0, int(2**n))

        shuffle_range = np.int64(((2**n))//((n**2)/2))
        
        for i in range(0, int(2**n), shuffle_range):

            #In place shuffle with instances RNG.(numpy.random.default_rng(seed))
            self.rng.shuffle(array[i: i + shuffle_range])

        return array.astype('int32')
    
    def integer_array(self, n, low=0, high=1000):
        return self.rng.integers(low, int(2**n), size=int(2**n)).astype('u8')

if __name__ == "__main__":
    # Testing structured data
    gen = ArrayGenerator(seed=12)
    N = 5
    x = np.arange(2**N, 0, -1)
    a = gen.structured_array(N)
    plt.barh(x, a)
    plt.show()