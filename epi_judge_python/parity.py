from test_framework import generic_test
from math import log2

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


def show_binary_comparison(func):
    def wrapped(*args) -> int:
        x, *_ = args
        x_bin = bin(x)
        ans = func(*args)
        ans_bin = bin(ans)
        print(f"{func.__name__}({str(args).strip('(),')}) = {ans}")
        print(f"bin({x}) = {x_bin}; bin({ans}) = {ans_bin}")
        return ans
    return wrapped


def isolate_lowest_set_bit(x: int) -> int:
    return x & ~(x - 1)

@show_binary_comparison
def propagate_rightmost_set(x: int) -> int:
    left_shift = int(log2(isolate_lowest_set_bit(x)))
    return x | ((1 << left_shift) - 1)

@show_binary_comparison
def modulo_pow2(x: int, pow2: int) -> int:
    # note pow2 is the integer exponent, so e.g. if pow2 = 4, then this computes mod 16
    return (x & ((1 << pow2) - 1))
