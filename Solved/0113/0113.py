# Problem No.: 113
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/path-sum-ii/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.sum = sum
        self.dfs(root, 0, [])
        return self.ans
        
    def dfs(self, root: TreeNode, tempSum: int, tempAns: List[int]) -> None:
        if not root.left and not root.right:
            if root.val + tempSum == self.sum:
                self.ans.append(tempAns + [root.val])
            return
        if root.left:
            self.dfs(root.left, tempSum + root.val, tempAns + [root.val])
        if root.right:
           self.dfs(root.right, tempSum + root.val, tempAns + [root.val]) 
            
        