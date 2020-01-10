# Problem No.: 101
# Solver:      Jinmin Goh
# Date:        20200109
# URL: https://leetcode.com/problems/symmetric-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        return self.check(root.left, root.right)
        
    def check(self, leftNode: TreeNode, rightNode: TreeNode) -> bool:
        if not leftNode and not rightNode:
            return True
        elif not leftNode or not rightNode:
            return False
        if leftNode.val != rightNode.val:
            return False
        else:
            return self.check(leftNode.left, rightNode.right) and self.check(leftNode.right, rightNode.left)
            