from test_framework import generic_test

from collections import Counter


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    if letter_text == "":
        return True

    let_char_counts = Counter(letter_text)
    del let_char_counts[" "]

    for c in magazine_text:
        if c in let_char_counts:
            let_char_counts[c] -= 1

        if let_char_counts[c] == 0:
            del let_char_counts[c]
        
        if not bool(let_char_counts):
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
