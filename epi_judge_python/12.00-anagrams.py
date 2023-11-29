from typing import List

from test_framework import generic_test, test_utils

from collections import defaultdict


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in dictionary:
        wk = get_word_key(word)
        anagrams[wk].append(word)

    return [list(anags) for anags in anagrams.values() if len(anags) >= 2]


def get_word_key(word):
    return "".join(sorted(word))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))


def find_anagrams_Onm(dictionary):
    pass
