# Problem No.: 368
# Solver:      Jinmin Goh
# Date:        20200615
# URL: https://leetcode.com/problems/largest-divisible-subset/

import sys

# O(n ^ 2) DP

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        cnt = [1] * len(nums)
        pre = [None] * len(nums)
        maxPos = None
        maxVal = 1
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if cnt[i] < cnt[j] + 1:
                        #print(i, j, nums[i], nums[j])
                        cnt[i] = cnt[j] + 1
                        pre[i] = j
            if cnt[i] > maxVal:
                maxPos = i
                maxVal = cnt[i]
            #print(cnt)
            #print(pre)
        if maxPos == None:
            return [nums[0]]
        
        
        ans = []
        while maxPos != None:
            ans.append(nums[maxPos])
            maxPos = pre[maxPos]
        
        ans = list(reversed(ans))
        return ans