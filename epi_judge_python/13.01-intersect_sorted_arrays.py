from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    m, n = len(A), len(B)

    res = []
    a, b = 0, 0
    while a < m and b < n:
        if A[a] == B[b]:
            if not res or A[a] != res[-1]:
                res.append(A[a])
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1
        else:
            raise Exception("this should never be reached")

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
