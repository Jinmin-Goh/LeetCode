# Problem No.: 315
# Solver:      Jinmin Goh
# Date:        20200318
# URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# good solution: https://www.geeksforgeeks.org/counting-inversions/
# good solution: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76607/C%2B%2B-O(nlogn)-Time-O(n)-Space-MergeSort-Solution-with-Detail-Explanation
# good solution: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution

# time: O(n log n) / space: O(n)

import sys

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        self.ans = [0] * len(nums)
        numPairList = list(enumerate(nums)) # making list of (index, value)
        self.mergeSort(numPairList)
        return self.ans
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left = nums[:len(nums) // 2]
        right = nums[len(nums) // 2:]
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        # in this point, left and right values are sorted
        for i in reversed(range(len(nums))):
            # in case of end value of left list is bigger than right list
            # all right list has smaller value than end value of left list(left[-1][1])
            # so we add len(right) into index of end of left list value.
            if not right or left and left[-1][1] > right[-1][1]:
                self.ans[left[-1][0]] += len(right)
                nums[i] = left.pop() 
            else:
                nums[i] = right.pop()
        # after merging, all values are sorted and considered for answer
        # Also, no longer compared with in-list values
        return nums
        