from test_framework import generic_test


def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drop the lowest set bit of x
    return result   # this has time complexity O(k), where k is is the number of bits set to 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
