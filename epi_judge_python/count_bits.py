from test_framework import generic_test


# O(n)
def count_bits_brute(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


# O(k), where k is is the number of bits set to 1
def count_bits_sparse(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += 1
        x &= x - 1  # drop the lowest set bit of x
    return num_bits


if __name__ == '__main__':
    print("brute-force:")
    generic_test.generic_test_main('count_bits.py', 'count_bits.tsv', count_bits_brute)
    print("sparse count:")
    exit(generic_test.generic_test_main('count_bits.py', 'count_bits.tsv', count_bits_sparse))
