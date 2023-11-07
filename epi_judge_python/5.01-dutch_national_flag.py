import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition_2pass(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    a_idx = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[a_idx] = A[a_idx], A[i]
            a_idx += 1
    b_idx = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[b_idx] = A[b_idx], A[i]
            b_idx -= 1


def dutch_flag_partition_1pass(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    a, b, c = 0, 0, len(A)
    while b < c:
        unclassified = A[b]
        if unclassified < pivot:
            A[a], A[b] = A[b], A[a]
            a += 1
            b += 1
        elif unclassified == pivot:
            b += 1
        else:
            c -= 1
            A[b], A[c] = A[c], A[b]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    # executor.run(functools.partial(dutch_flag_partition_2pass, pivot_idx, A))
    executor.run(functools.partial(dutch_flag_partition_1pass, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
