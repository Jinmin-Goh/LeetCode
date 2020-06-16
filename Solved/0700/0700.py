# Problem No.: 700
# Solver:      Jinmin Goh
# Date:        20200616
# URL: https://leetcode.com/problems/search-in-a-binary-search-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        node = root
        while True:
            if node.val == val:
                return node
            elif node.val > val:
                if not node.left:
                    return None
                node = node.left
            else:
                if not node.right:
                    return None
                node = node.right