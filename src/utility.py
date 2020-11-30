import functools
import time
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
from statistics import mean, stdev



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
        return np.arange(0,2**n)

    def reversed_array(self, n):
        return np.arange(2**n, 0, -1)
    
    def random_array(self, n):
        return self.rng.random(2**n)

    def structured_array(self, n):
        """
        Creates an array with an obvious structure, already ascending.
        """

        array = np.arange(0,2**n)

        shuffle_range = np.int64((2**n)//(n*(n/2)))
        
        for i in range(0, 2**n, shuffle_range):

            #In place shuffle with instances RNG.(numpy.random.default_rng(seed))
            self.rng.shuffle(array[i: i + shuffle_range])

        return array

if __name__ == "__main__":

    # Testing structured data
    gen = ArrayGenerator(seed=12)

    a = gen.structured_array(6)
    plt.plot(a)
    plt.show()


def random_int_generator(length):
    """Creates list of integers of given length - with random order"""
    return list((np.random.randint(-length, length, size=length)))

def random_float_generator(length):
    """Creates list of decimal numbers of given length - with random order"""
    return list((np.random.uniform(-length, length, size=length)))

def ordered_generator(length):
    """Creates list of numbers of given length - with acsending order"""
    return list(np.arange(1, length))

def reversed_generator(length):
    """Creates list of numbers of given length - with descending order"""
    return list(np.flipud(ordered_generator(length)))


def benchmark(algorithm, given_list):
    """ Returns the runtime of a sorting algorithim on a given list."""
    
    rng = np.random.default_rng(12235) 
    clock = timeit.Timer(stmt='sort_func(copy(data))', globals={'sort_func': algorithm,
                                                                'data': given_list , 'copy': copy.copy})
    n_ar, t_ar = clock.autorange()
    t = clock.repeat(repeat=10, number=n_ar)
    return np.average(t)/n_ar



def benchmark_algos_and_types(algorithm, list_size):
    """ Returns the time for given list type and return a dictionary with the results. """
    
    integer_results = [( _ , benchmark(algorithm, random_int_generator(_))) 
                      for _ in range(0, list_size, 50)]
    
    float_results = [( _ , benchmark(algorithm, random_float_generator(_))) 
                     for _ in range(0, list_size, 50)]
    
    ascending_results = [( _ , benchmark(algorithm, ordered_generator(_))) 
                         for _ in range(0, list_size, 50)]
    
    descending_result = [( _ , benchmark(algorithm, reversed_generator(_))) 
                         for _ in range(0, list_size, 50)]
    
    
    all_results = {'Random integers' : integer_results, 
                   'Random float' : float_results, 
                   'Ascending integers' : ascending_results,
                   'Descending integers' : descending_result}
    
    return all_results