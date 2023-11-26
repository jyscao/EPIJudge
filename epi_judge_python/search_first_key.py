from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    return _binary_search(A, k, 0)

def _binary_search(A, k, idx_offset):
    if A == []:
        return -1

    m = len(A) // 2
    p = A[m]
    if p == k:
        possible_prev_idx = _binary_search(A[:m], k, idx_offset)
        return min(m + idx_offset, float("inf") if possible_prev_idx == -1 else possible_prev_idx)
    elif p > k:
        return _binary_search(A[:m], k, idx_offset)
    elif p < k:
        return _binary_search(A[m + 1:], k, idx_offset + m + 1)
    else:
        raise Exception("this should never be reached")


# NOTE: the book solution is 2 orders of mag faster when executing all tests
def search_first_of_k_book(A: List[int], k: int) -> int:
    left, right = 0, len(A) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            res = mid
            right = mid - 1
        elif A[mid] < k:
            left = mid + 1
        else:
            raise Exception("this should never be reached")

    return res

 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       # search_first_of_k))
                                       search_first_of_k_book))



def search_first_gt_k(A: List[int], k: int) -> int:
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] == k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
        else:
            raise Exception("this should never be reached")

    ans = mid + (A[mid] <= k) 

    return ans if ans < len(A) else -1
