# Problem No.: 108
# Solver:      Jinmin Goh
# Date:        20200112
# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            ans = TreeNode(nums[len(nums) // 2])
            ans.left = self.sortedArrayToBST(nums[:len(nums) // 2])
            ans.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        return ans