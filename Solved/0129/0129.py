# Problem No.: 129
# Solver:      Jinmin Goh
# Date:        20200119
# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/

import sys

# time: O(n) / space: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.dfs(root, "")
        return self.ans
        
    def dfs(self, root: TreeNode, tempAns: str) -> None:
        if not root.left and not root.right:
            self.ans += int(tempAns + str(root.val))
            return
        if root.left:
            self.dfs(root.left, tempAns + str(root.val))
        if root.right:
            self.dfs(root.right, tempAns + str(root.val))
            