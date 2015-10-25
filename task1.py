__author__ = 'EnDoR'
from statistics import median


def check_sizes(array_1, array_2):
    if len(array_1) != len(array_2):
        raise Exception("Sizes of array are not equal.")
    if len(array_1) == 0:
        raise Exception("Sizes of array are equal to zero")


def simple_median_statistics(array_1, array_2):
    return median(array_1 + array_2)


def simple_median(array_1, array_2):
    sorted_combination = sorted(array_1 + array_2)
    n = len(array_1)
    return 0.5 * (sorted_combination[n-1] + sorted_combination[n])


def eff_median(array_1, array_2):
    size = len(array_1)
    if array_1[size - 1] <= array_2[0]:
        return 0.5 * (array_1[size - 1] + array_2[0])
    elif array_2[size - 1] <= array_1[0]:
        return 0.5 * (array_2[size - 1] + array_1[0])
    i_1 = 0
    i_2 = 0
    min1 = 0
    max1 = 0
    while i_1 + i_2 < size - 1:
        if array_1[i_1] > array_2[i_2]:
            i_2 += 1
        else:
            i_1 += 1
    if array_1[i_1] > array_2[i_2]:
        min1 = array_2[i_2]
        i_2 += 1
    else:
        min1 = array_1[i_1]
        i_1 += 1
    if array_1[i_1] > array_2[i_2]:
        max1 = array_2[i_2]
    else:
        max1 = array_1[i_1]
    return 0.5 * (min1 + max1)


if __name__ == "__main__":
    arr_1 = [int(x) for x in input("Input first array: ").split()]
    arr_2 = [int(x) for x in input("Input second array: ").split()]

    check_sizes(arr_1, arr_2)
    print(eff_median(arr_1, arr_2))


