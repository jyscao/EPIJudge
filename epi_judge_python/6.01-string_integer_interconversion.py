from test_framework import generic_test
from test_framework.test_failure import TestFailure


from math import log10, floor
dig_to_char = {d: c for d, c in enumerate("0123456789")}
def int_to_string_self(x: int) -> str:
    if x == 0:
        return "0"

    sign, x = "-" if x < 0 else "", abs(x)
    int_str_ls = []
    highest_pow = floor(log10(abs(x)))
    for p in range(highest_pow, -1, -1):
        mag = 10 ** p
        dig = x // mag
        int_str_ls.append(dig_to_char[dig])
        x -= dig * mag

    return sign + "".join(int_str_ls)


char_to_dig = {c: d for d, c in enumerate("0123456789")}
def string_to_int_self(s: str) -> int:
    if s[0] == "-":
        sign, n, s = -1, len(s) - 1, s[1:]
    elif s[0] == "+":
        sign, n, s = 1, len(s) - 1, s[1:]
    else:
        sign, n, s  = 1, len(s), s
    
    magnitude = 0
    for i, c in enumerate(s):
        magnitude += char_to_dig[c] * 10**(n - i - 1)

    return sign * magnitude


# NOTE: the book soln doesn't require any imported functions from math, by
# using chr() & ord(); it also transparently handles the case where x == 0.
def int_to_string_book(x: int) -> str:
    sign, x = "-" if x < 0 else "", abs(x)
    str_int_ls = []
    while True:
        # the key insight here is that the least-significant digit can be
        # extracted using modulo-10
        str_int_ls.append(chr(ord("0") + x % 10))
        x //= 10
        if x == 0:
            break
    return sign + "".join(reversed(str_int_ls))


from functools import reduce
def string_to_int_book(s: str) -> int:
    return (-1 if s[0] == "-" else 1) * reduce(
        lambda curr_val, char: curr_val * 10 + "0123456789".index(char),
        s[(s[0] in "-+"):],     # True is coverted to 1, while False to 0
        0
    )


def wrapper(x, s):
    if int(int_to_string_book(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int_book(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
