from test_framework import generic_test


# O(n)
def parity_brute(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# O(k), where k is is the number of bits set to 1
def parity_sparse(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drop the lowest set bit of x
    return result


# O(n/L)
def parity_precompute(x: int) -> int:
    bit_mask = 0xFFFF
    result = (
        PCACHE[x >> (3 * L)] ^
        PCACHE[x >> (2 * L) & bit_mask] ^
        PCACHE[x >> (1 * L) & bit_mask] ^
        PCACHE[x >> (0 * L) & bit_mask]
    )
    return result


# O(log(n))
def parity_assoc(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

def _get_parities_cache(L):
    cache = {}
    for i in range(2 ** L):
        # cache[i] = parity_sparse(i)
        cache[i] = parity_assoc(i)
    return cache

L = 16  # word size
PCACHE = _get_parities_cache(L)


if __name__ == '__main__':
    print("brute-force:")
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity_brute)
    print("sparse count:")
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity_sparse)
    print("precompute:")
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity_precompute)
    print("XOR against self:")
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity_assoc))
