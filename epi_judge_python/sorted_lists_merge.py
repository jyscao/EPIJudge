from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if L1 is None:
        return L2
    elif L2 is None:
        return L1

    current, other = (L1, L2) if L1.data <= L2.data else (L2, L1)
    head = current
    while True:
        next_on_curr = current.next
        if next_on_curr is None:
            current.next = other
            break

        if next_on_curr.data <= other.data:
            current = next_on_curr
        else:
            current.next, other = other, current.next

        if current.next is None:
            current.next = other
            break

    return head



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
