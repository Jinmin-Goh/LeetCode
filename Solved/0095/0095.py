# Problem No.: 95
# Solver:      Jinmin Goh
# Date:        20200106
# URL: https://leetcode.com/problems/unique-binary-search-trees-ii/

import sys

# solution link: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31592/Recursive-python-solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        ans = self.makeFunc(1, n)
        return ans
    
    def makeFunc(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        temp_ans = []
        for i in range(start, end + 1):
            for l in self.makeFunc(start, i - 1) or [None]:
                for r in self.makeFunc(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    temp_ans.append(node)
        return temp_ans