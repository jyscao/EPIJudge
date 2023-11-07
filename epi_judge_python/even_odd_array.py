import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return x % 2 == 1

def even_odd_self(A: List[int]) -> None:
    n = len(A)
    i, j = 0, -1
    while i <= j % n:
        if is_even(A[i]):
            i += 1
        else:
            while abs(j) < n and is_odd(A[j]):
                j -= 1
            else:
                if i >= j % n:
                    break
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1


# NOTE: the key difference b/w the book vs. our soln is that the book's soln
# doesn't care to avoid swapping an odd at the beginning w/ another odd near
# the end; as such swaps will decrement the end-odd pointer anyway, so
# eventually an even near the end will be reached and get swapped with the
# same-indexed odd number near the beginning
def even_odd_book(A: List[int]) -> None:
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    # executor.run(functools.partial(even_odd_self, A))
    executor.run(functools.partial(even_odd_book, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
