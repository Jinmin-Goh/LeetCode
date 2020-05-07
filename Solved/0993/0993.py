# Problem No.: 993
# Solver:      Jinmin Goh
# Date:        20200507
# URL: https://leetcode.com/problems/cousins-in-binary-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [root]
        while stack:
            temp = []
            flag = False
            while stack:
                node = stack.pop()
                if node.val == x or node.val == y:
                    if flag:
                        return True
                    else:
                        flag = True
                if node.left and node.right:
                    if node.left.val in [x, y] and node.right.val in [x, y]:
                        return False
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if flag:
                return False
            stack = temp[:]
            