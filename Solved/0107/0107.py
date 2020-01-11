# Problem No.: 107
# Solver:      Jinmin Goh
# Date:        20200111
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        nodeList = [root]
        while nodeList:
            tempList = []
            tempAns = []
            for i in nodeList:
                tempAns.append(i.val)
                if i.left:
                    tempList.append(i.left)
                if i.right:
                    tempList.append(i.right)
            ans = [tempAns] + ans
            nodeList = tempList[:]
        return ans