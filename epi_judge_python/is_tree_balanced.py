from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    is_balanced, _height = check_balanced(tree)
    # print()
    # print(_height)
    return is_balanced


def check_balanced(tree):
    if not tree:
        return True, -1

    left_balanced, left_height = check_balanced(tree.left)
    if not left_balanced:
        return False, None

    right_balanced, right_height = check_balanced(tree.right)
    if not right_balanced:
        return False, None

    is_balanced = abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1
    return is_balanced, height


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
