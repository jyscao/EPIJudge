from test_framework import generic_test


# O(n)
def parity_brute(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# O(k), where k is is the number of bits set to 1
def parity_sparse_drop(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drop the lowest set bit of x
    return result


if __name__ == '__main__':
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity_brute)
    print()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity_sparse_drop))
