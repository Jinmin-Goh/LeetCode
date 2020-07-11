# Problem No.: 662
# Solver:      Jinmin Goh
# Date:        20200711
# URL: https://leetcode.com/problems/maximum-width-of-binary-tree/

import sys
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        deque = collections.deque([[root, 1]])
        ans = 1
        while deque:
            deque.append(None)
            lVal = None
            rVal = None
            while True:
                temp = deque.popleft()
                if temp == None:
                    break
                if not lVal:
                    lVal = temp[1]
                    rVal = temp[1]
                else:
                    rVal = max(rVal, temp[1])
                if temp[0].left:
                    deque.append([temp[0].left, temp[1] * 2])
                if temp[0].right:
                    deque.append([temp[0].right, temp[1] * 2 + 1])
            #print(lVal, rVal, deque)
            if not(lVal or rVal):
                break
            
            ans = max(ans, rVal - lVal + 1)
        return ans
                    