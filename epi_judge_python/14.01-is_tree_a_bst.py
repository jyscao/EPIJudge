from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst_book1(tree: BinaryTreeNode) -> bool:
    def keys_within_bounds(tree, lower, upper):
        if not tree:
            return True

        node_valid  = lower <= tree.data <= upper
        left_valid  = keys_within_bounds(tree.left, lower, tree.data)
        right_valid = keys_within_bounds(tree.right, tree.data, upper)

        return node_valid and left_valid and right_valid
        
    return keys_within_bounds(tree, -float("inf"), float("inf"))


def is_binary_tree_bst_book2(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    def get_data(tree):
        left_vals  = get_data(tree.left)  if tree.left  else []
        right_vals = get_data(tree.right) if tree.right else []

        return left_vals + [tree.data] + right_vals
    
    in_order_vals = get_data(tree)
    return in_order_vals == sorted(in_order_vals)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_book2))
