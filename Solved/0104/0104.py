# Problem No.: 104
# Solver:      Jinmin Goh
# Date:        20200109
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodeList = [root]
        ans = 0
        while nodeList:
            tempList = []
            for i in nodeList:
                if i.left:
                    tempList.append(i.left)
                if i.right:
                    tempList.append(i.right)
            ans += 1
            nodeList = tempList[:]
        return ans