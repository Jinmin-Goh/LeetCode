# Problem No.: 230
# Solver:      Jinmin Goh
# Date:        20200312
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        countRoot = TreeNode((0, 0))
        countRoot.val = self.countDFS(root, countRoot)
        count = countRoot.val[0] + 1
        walker = root
        cWalker = countRoot
        while count != k:
            #print(walker.val, cWalker.val, count)
            if count < k:
                count = count + cWalker.right.val[0] + 1
                walker = walker.right
                cWalker = cWalker.right
            else:
                count = count - cWalker.val[0] + cWalker.left.val[0]
                walker = walker.left
                cWalker = cWalker.left
        return walker.val
        
    def countDFS(self, root: TreeNode, countRoot: TreeNode) -> (int, int):
        if not(root.left or root.right):
            countRoot.val = (0, 0)
            return (0, 0)
        lTemp = (-1, 0)
        rTemp = (-1, 0)
        if root.left:
            countRoot.left = TreeNode((0, 0))
            lTemp = self.countDFS(root.left, countRoot.left)
        if root.right:
            countRoot.right = TreeNode((0, 0))
            rTemp = self.countDFS(root.right, countRoot.right)
        countRoot.val = (sum(lTemp) + 1, sum(rTemp) + 1)
        return countRoot.val