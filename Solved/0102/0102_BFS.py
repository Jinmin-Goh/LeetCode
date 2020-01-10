# Problem No.: 102
# Solver:      Jinmin Goh
# Date:        20200109
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS method solution

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        nodeList = [root]
        while nodeList:
            ans.append([])
            tempList = []
            for i in nodeList:
                ans[-1].append(i.val)
                if i.left:
                    tempList.append(i.left)
                if i.right:
                    tempList.append(i.right)
            nodeList = tempList[:]
        return ans
        