__author__ = 'EnDoR'
import itertools

def infinite_sequence():
    for number in itertools.count(1):
        string_number = str(number)
        for s in string_number:
            yield s


def prefix(pattern):
    len_pattern = len(pattern)
    pref = [0] * len_pattern
    k = 0
    for q in range(1, len_pattern):
        while k > 0 and pattern[k] != pattern[q]:
            k = pref[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pref[q] = k
    return pref


def find_match(sequence, pattern):
    len_pattern = len(pattern)
    pref = prefix(pattern)
    q = 0
    index = 0
    for i in sequence:
        index += 1
        while q > 0 and pattern[q] != i:
            q = pref[q - 1]
        if pattern[q] == i:
            q += 1
        if q == len_pattern:
            return index - len_pattern + 1


if __name__ == "__main__":
    arr = [int(x) for x in input("Input array of patterns: ").split()]
    for a in arr:
        sequence = infinite_sequence()
        print(find_match(sequence, str(a)))
