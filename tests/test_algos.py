"""
Test-suite for sorting algos
"""
import unittest
import numpy as np

from src.linear_sorting_algorithms import radixsort
from src.quadratic_sorting_algorithms import bubble_sort, insertion_sort
from src.subquad_sorting_algorithms import  quicksort, mergesort, iterative_quicksort, iterative_quicksort_shufffle
from src.combined_sorting_algorithm import mergesort_combined


class TestSortingAlgorithms(unittest.TestCase):
    def get_int_arr(self):
        return [18,5,100,3,1,19,6,0,7,4,2]

    def get_float_arr(self):
        return [123.342, 54352.8765, 432523.435432, 765436.3241, 4215213.534241, 643123.124552]

    def get_random_array(self):
        return np.random.random(1000)

    def get_same_number_array(self):
        return [1]*10

    def get_already_sorted(self):
        return np.arange(10)

    def get_empty_array(self):
        return list()

    def get_one_element_array(self):
        return [1]

    def check_if_ascending(self, A):
        for i in range( 1, len(A)):
            if A[i - 1] > A[i]:
                return False

        return True

    
    
    
    def _test_sorting_algorithm(self, function):
        A = self.get_int_arr()
        function(A)
        if not self.check_if_ascending(A):
            self.fail(f"{function.__name__} failed on integers")

        B = self.get_float_arr()
        function(B)
        if not self.check_if_ascending(B):
            self.fail(f"{function.__name__} failed on floats")

        C = self.get_random_array()
        function(C)
        if not self.check_if_ascending(C):
            self.fail(f"{function.__name__} failed on random numbers")

        D = self.get_same_number_array()
        function(D)
        self.assertEqual(D, self.get_same_number_array(), msg=f"{function.__name__} failed on same numbers")

        E =  self.get_already_sorted()
        function(E)
        if not self.check_if_ascending(C):
            self.fail(f"{function.__name__} failed on already sorted numbers")

        F = self.get_one_element_array()
        if F != self.get_one_element_array():
            self.fail(f"{function.__name__} failed on single number")

        G =  self.get_empty_array()
        function(E)
        if G != self.get_empty_array():
            self.fail(f"{function.__name__} failed on empty")

    def test_all_algoritms(self):
        self._test_sorting_algorithm(bubble_sort)
        self._test_sorting_algorithm(insertion_sort)
        self._test_sorting_algorithm(mergesort)
        self._test_sorting_algorithm(mergesort_combined)
        self._test_sorting_algorithm(quicksort)
        self._test_sorting_algorithm(iterative_quicksort)
        self._test_sorting_algorithm(iterative_quicksort_shufffle)
        
    def test_radix(self):
        A = self.get_int_arr()
        radixsort(A)
        if not self.check_if_ascending(A):
            self.fail("Radixsort failed")


if __name__ == '__main__':
    unittest.main()