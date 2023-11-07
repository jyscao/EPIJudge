from list_node import ListNode
from test_framework import generic_test


def search_list_recurse(L: ListNode, key: int) -> ListNode:
    if L.data == key:
        return L
    else:
        return ListNode(-1, None) if L.next is None else search_list_recurse(L.next, key)


def search_list_iter(L:ListNode, key: int) -> ListNode:
    while L and L.data != key:
        L = L.next
    else:
        return L


def search_list_wrapper(L, key):
    # result = search_list_recurse(L, key)
    result = search_list_iter(L, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_list.py',
                                       'search_in_list.tsv',
                                       search_list_wrapper))
