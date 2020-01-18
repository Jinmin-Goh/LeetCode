# Problem No.: 124
# Solver:      Jinmin Goh
# Date:        20200118
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

import sys

# solution link: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39869/Simple-O(n)-algorithm-with-one-traversal-through-the-tree
# one time traversal solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -(2 ** 31)
        self.dfs(root)
        return self.ans
    
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        lVal = max(0, self.dfs(root.left))
        rVal = max(0, self.dfs(root.right))
        self.ans = max(self.ans, lVal + rVal + root.val)
        return root.val + max(lVal, rVal)
        