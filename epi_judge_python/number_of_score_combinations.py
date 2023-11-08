from typing import List

from test_framework import generic_test

import numpy as np


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
# def num_combinations_for_final_score(final_score, individual_play_scores):
    # individual_play_scores.sort()     # NOTE: sorting is not needed
    scores_combo = np.zeros((len(individual_play_scores), final_score + 1,), dtype=int)
    for p in range(len(individual_play_scores)):
        play_score = individual_play_scores[p]
        for s in range(0, final_score + 1):
            if s == 0:
                scores_combo[p, 0] = 1
            else:
                without_play = scores_combo[p - 1, s] if p >= 1 else 0
                with_play = scores_combo[p, s - play_score] if s >= play_score else 0
                scores_combo[p, s] = without_play + with_play
    return scores_combo[-1, -1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
