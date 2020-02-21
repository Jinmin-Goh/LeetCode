# Problem No.: 337
# Solver:      Jinmin Goh
# Date:        20200221
# URL: https://leetcode.com/problems/house-robber-iii/

import sys

# good solution link: https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.DFS(root))
    
    def DFS(self, root: TreeNode) -> None:
        # now: max money earned if root is robbed
        # later: max money earned if root is not robbed
        if not root: return (0, 0)
        leftVal = self.DFS(root.left)
        rightVal = self.DFS(root.right)
        
        # rob now
        now = root.val + leftVal[1] + rightVal[1]
        # rob later
        later = max(leftVal) + max(rightVal)
        return (now, later)