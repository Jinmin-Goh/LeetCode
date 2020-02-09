# Problem No.: 236
# Solver:      Jinmin Goh
# Date:        20200209
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

import sys

# DFS solution, time: O(log n) avg O(n) worst / space: O(log n) avg O(n) worst
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.DFS(root, [], p.val)
        qPath = self.DFS(root, [], q.val)
        i = 0
        #print(pPath, qPath)
        if len(pPath) <= len(qPath) and pPath[-1] == qPath[len(pPath) - 1]:
            pos = len(pPath)
        elif len(pPath) >= len(qPath) and pPath[len(qPath) - 1] == qPath[-1]:
            pos = len(qPath)
        else:
            while pPath[i] == qPath[i]:
                i += 1
            pos = i
        ans = root
        #print(pPath, qPath, pos)
        for i in range(1, pos):
            if ans.right and ans.right.val == pPath[i]:
                ans = ans.right
            if ans.left and ans.left.val == pPath[i]:
                ans = ans.left
        return ans
        
    def DFS(self, root: TreeNode, path: List[int], target: int) -> List[int]:
        #print(root.val, path, target)
        if root.val == target:
            return path + [root.val]
        else:
            tempLeft = None
            tempRight = None
            if root.left:
                tempLeft = self.DFS(root.left, path + [root.val], target)
            if root.right:
                tempRight = self.DFS(root.right, path + [root.val], target)
            if tempLeft:
                return tempLeft
            if tempRight:
                return tempRight