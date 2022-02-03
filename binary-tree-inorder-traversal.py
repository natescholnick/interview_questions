# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    if root != None:
        if root == []:
            return []
        head = [root[0]]
        left = []
        right = []
        for r in range(1, math.floor(math.log(len(root), 2)) + 1):
            left = left + root[2**r-1: 2**r+r-1]
            right = right + root[2**r+r-1:2**(r+1)-1]
        return inorderTraversal(left) + head + inorderTraversal(right)


# print(inorderTraversal([1, None, 2, 3]))

# 0  2^r - 1 <-- --> 2^r+1 - 1
# 12
# 34 56
# 789 10 11 12 13 14

# 1 3 4 7 8 9 10

print(inorderTraversal([0, 1, 2]))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
