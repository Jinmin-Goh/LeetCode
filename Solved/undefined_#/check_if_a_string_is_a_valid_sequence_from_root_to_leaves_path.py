# Problem No.: ???
# Solver:      Jinmin Goh
# Date:        20200430
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        currList = [root]
        flag = False
        while currList and arr and not flag:
            temp = []
            for i in currList:
                if i.val == arr[0]:
                    if not(i.left or i.right) and len(arr) == 1:
                        flag = True
                        break
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
            arr.pop(0)
            currList = temp[:]
            
        return flag