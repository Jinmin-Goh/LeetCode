# Problem No.: 102
# Solver:      Jinmin Goh
# Date:        20200107
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS search solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.bfs(root, 0)
        return self.ans
        
    def bfs(self, root: TreeNode, n: int) -> None:
        if not root:
            return
        if len(self.ans) - 1 < n:
            self.ans.append([])
        self.ans[n].append(root.val)
        self.bfs(root.left, n + 1)
        self.bfs(root.right, n + 1)
        