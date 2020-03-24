# Problem No.: 350
# Solver:      Jinmin Goh
# Date:        20200325
# URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/

import sys

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dict = {}
        num2Dict = {}
        ans = []
        for i in nums1:
            if i not in num1Dict:
                num1Dict[i] = 1
            else:
                num1Dict[i] += 1
        for i in nums2:
            if i not in num2Dict:
                num2Dict[i] = 1
            else:
                num2Dict[i] += 1
        for i in num1Dict:
            if i in num2Dict:
                temp = min(num1Dict[i], num2Dict[i])
                for j in range(temp):
                    ans.append(i)
        return ans    