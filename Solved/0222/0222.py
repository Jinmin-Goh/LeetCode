# Problem No.: 222
# Solver:      Jinmin Goh
# Date:        20200624
# URL: https://leetcode.com/problems/count-complete-tree-nodes/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        temp = 1
        temp += self.countNodes(root.left)
        temp += self.countNodes(root.right)
        return temp
    