from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists_self(L1: Optional[ListNode],
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


def merge_two_sorted_lists_book(L1: Optional[ListNode],
                                L2: Optional[ListNode]) -> Optional[ListNode]:

    # NOTE: this is also known as a "sentinel"; its use allows us to avoid
    # initializing the current working list to one of L1 and L2, and go
    # straight into the loop that compares their values and follows them
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       # merge_two_sorted_lists_self))
                                       merge_two_sorted_lists_book))


from doubly_list_node import DoublyListNode
def sorted_doubly_linked_lists_merge(L1: Optional[DoublyListNode],
                                     L2: Optional[DoublyListNode],
                                     ) -> Optional[DoublyListNode]:
    dummy_head = tail = DoublyListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1.prev, L1 = L1, tail, L1.next
        else:
            tail.next, L2.prev, L2 = L2, tail, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next
