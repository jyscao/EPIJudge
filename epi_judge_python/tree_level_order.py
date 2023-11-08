from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    result = []
    curr_level_nodes, next_level_nodes = [tree], []
    while curr_level_nodes:
        result.append([node.data for node in curr_level_nodes])
        for node in curr_level_nodes:
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        curr_level_nodes, next_level_nodes = next_level_nodes, []

    return result


def binary_tree_depth_order_book(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return result
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [child
            for node in curr_depth_nodes
            for child in (node.left, node.right)
            if child
        ]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
                                       # binary_tree_depth_order_book))


def binary_tree_depth_avg(tree: BinaryTreeNode) -> List[float]:
    if not tree:
        return []

    result = []
    curr_level_nodes, next_level_nodes = [tree], []
    while curr_level_nodes:
        result.append(sum(node.data for node in curr_level_nodes) / len(curr_level_nodes))
        for node in curr_level_nodes:
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        curr_level_nodes, next_level_nodes = next_level_nodes, []

    return result
