"""
Test-suite for sorting algos
"""
import unittest
import numpy as np

from src.linear_sorting_algorithms import radixsort
from src.quadratic_sorting_algorithms import bubble_sort, insertion_sort
from src.subquad_sorting_algorithms import quicksort, mergesort
from src.combined_sorting_algorithm import mergesort_combined


class TestSortingAlgorithms(unittest.TestCase):
    def get_int_arr(self):
        return [18,5,100,3,1,19,6,0,7,4,2]

    def get_float_arr(self):
        return [123.342, 54352.8765, 432523.435432, 765436.3241]

    def get_random_array(self):
        return np.random.rand(100)

    def check_if_ascending(self, A):
        for i in range( 1, len(A) ):
            if A[i - 1] > A[i]:
                return False

        return True

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_radix(self):
        A = self.get_int_arr()
        radixsort(A)
        if not self.check_if_ascending(A):
            self.fail("Radixsort failed")
       
    
    def test_bubblesort(self):
        A = self.get_int_arr()
        bubble_sort(A)
        if not self.check_if_ascending(A):
            self.fail("Bubble failed on integers")

        B = self.get_float_arr()
        bubble_sort(B)
        if not self.check_if_ascending(B):
            self.fail("Bubblesort failed on floats")

        C = self.get_random_array()
        bubble_sort(C)
        if not self.check_if_ascending(C):
            self.fail("Bubblesort failed on random numbers")


    def test_insertion_sort(self):
        A = self.get_int_arr()
        insertion_sort(A)
        if not self.check_if_ascending(A):
            self.fail("Insertion sort failed on integers")

        B = self.get_float_arr()
        insertion_sort(B)
        if not self.check_if_ascending(B):
            self.fail("Insertion sort failed on floats")

        C = self.get_random_array()
        insertion_sort(C)
        if not self.check_if_ascending(C):
            self.fail("Insertion sort failed on random numbers")


    def test_merge_sort(self):
        A = self.get_int_arr()
        mergesort(A)
        if not self.check_if_ascending(A):
            self.fail("mergesort failed on integers")

        B = self.get_float_arr()
        mergesort(B)
        if not self.check_if_ascending(B):
            self.fail("mergesort failed on floats")

        C = self.get_random_array()
        mergesort(C)
        if not self.check_if_ascending(C):
            self.fail("mergesort failed on random numbers")


    def test_merge_sort_combined(self):
        A = self.get_int_arr()
        mergesort_combined(A)
        if not self.check_if_ascending(A):
            self.fail("mergesort combined with insertion failed on integers")

        B = self.get_float_arr()
        mergesort_combined(B)
        if not self.check_if_ascending(B):
            self.fail("mergesort combined with insertion failed on floats")

        C = self.get_random_array()
        mergesort_combined(C)
        if not self.check_if_ascending(C):
            self.fail("mergesort combined with insertion failed on random numbers")

if __name__ == '__main__':
    unittest.main()