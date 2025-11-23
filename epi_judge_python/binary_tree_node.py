from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()


# TODO/FIXME: the tree element's order are fucked up
def build_bt_from_list(bt_list):
    bt_list_rev = list(reversed(bt_list))

    curr_depth_nodes = [BinaryTreeNode(data=bt_list_rev.pop()[0])]
    ans = curr_depth_nodes[0]
    while bt_list_rev:
        next_depth_data = bt_list_rev.pop()
        assert 2 * len(curr_depth_nodes) == len(next_depth_data)

        next_depth_nodes = []
        for i, node in enumerate(curr_depth_nodes):
            node.left = BinaryTreeNode(data=next_depth_data[2*i])
            node.right= BinaryTreeNode(data=next_depth_data[2*i+1])
            next_depth_nodes.append(node.left)
            next_depth_nodes.append(node.right)
        curr_depth_nodes = next_depth_nodes

    return ans
