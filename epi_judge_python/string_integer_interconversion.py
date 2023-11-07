from test_framework import generic_test
from test_framework.test_failure import TestFailure
from math import log10, floor


dig_to_char = {d: c for d, c in enumerate("0123456789")}
def int_to_string(x: int) -> str:
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
def string_to_int(s: str) -> int:
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


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
