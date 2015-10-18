__author__ = 'EnDoR'
from statistics import median
import timeit
import numpy.random as nprnd


def simple_median_statistics(array_1, array_2):
    return median(array_1 + array_2)


def simple_median(array_1, array_2):
    sorted_combination = sorted(array_1 + array_2)
    n = len(array_1)
    return 0.5 * (sorted_combination[n-1] + sorted_combination[n])


def check_sizes(array_1, array_2):
    if len(array_1) != len(array_2):
        raise Exception("Sizes of array are not equal.")


def eff_median(array_1, array_2):
    size = len(array_1)
    i_1 = 0
    i_2 = 0
    while i_1 + i_2 < size - 1:
        if array_1[i_1] < array_2[i_2]:
            i_1 += 1
        else:
            i_2 += 1
    return 0.5 * (array_1[i_1] + array_2[i_2])

# arr_1 = [int(x) for x in input("Input first array: ").split()]
# arr_2 = [int(x) for x in input("Input second array: ").split()]

# check_sizes(arr_1, arr_2)

# print(simple_median_statistics(arr_1, arr_2))
# print(simple_median(arr_1, arr_2))
# print(eff_median(arr_1, arr_2))

a = sorted(nprnd.randint(0, 1000, 10000))
b = sorted(nprnd.randint(0, 1000, 10000))


print(timeit.timeit("simple_median_statistics(a,b)", number=10000,
                    setup="from __main__ import simple_median_statistics, a, b"))
print(timeit.timeit("simple_median(a, b)", number=1000, setup="from __main__ import simple_median, a, b"))
print(timeit.timeit("eff_median(a, b)", number=1000, setup="from __main__ import eff_median, a, b"))
