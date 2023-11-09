from typing import List

from test_framework import generic_test

import heapq as hq


def merge_sorted_arrays_naive(sorted_arrays: List[List[int]]) -> List[int]:
    # return list(hq.merge(*sorted_arrays))
    flat_array = [i for subarr in sorted_arrays for i in subarr]
    hq.heapify(flat_array)
    return [hq.heappop(flat_array) for _ in range(len(flat_array))]


def merge_sorted_arrays_book_method(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []

    for i, ls in enumerate(sorted_arrays):
        hq.heappush(heap, (ls[0], i, 0))

    res = []
    while heap:
        curr_min, L, idx = hq.heappop(heap)
        res.append(curr_min)

        if idx + 1 < len(sorted_arrays[L]):
            idx += 1
            hq.heappush(heap, (sorted_arrays[L][idx], L, idx))
    return res


# def merge_sorted_arrays_book_copy(sorted_arrays: List[List[int]]) -> List[int]:
def merge_sorted_arrays_book_copy(sorted_arrays):
    heap = []
    sorted_iters = [iter(sub_arr) for sub_arr in sorted_arrays]

    for it_idx, s_it in enumerate(sorted_iters):
        hq.heappush(heap, (next(s_it), it_idx,))

    res = []
    while heap:
        curr_min, it_idx = hq.heappop(heap)
        res.append(curr_min)

        iter_next = next(sorted_iters[it_idx], None)
        if iter_next is not None:
            hq.heappush(heap, (iter_next, it_idx))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays_naive))
                                       # merge_sorted_arrays_book_method))
                                       # merge_sorted_arrays_book_copy))

    # NOTE: the book solns in theory have better time complexities of O(nlogk)
    # by taking advantage of the fact that elements of each sub-list are
    # already sorted; but the "naive" implementation that uses heapq.heapify
    # (O(n) time complexity) is actually faster in practice, even though it
    # also ends up being O(nlogk) due to the heapq.heappush() calls.
