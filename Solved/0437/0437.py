# Problem No.: 437
# Solver:      Jinmin Goh
# Date:        20200225
# URL: https://leetcode.com/problems/path-sum-iii/

import sys

# Brute-force method
# good solution link: https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.BF(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
        
    def BF(self, root: TreeNode, target: int) -> int:
        if root:
            return int(root.val == target) + self.BF(root.left, target - root.val) + self.BF(root.right, target - root.val)
        return 0