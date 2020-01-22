# Problem No.: 135
# Solver:      Jinmin Goh
# Date:        20200122
# URL: https://leetcode.com/problems/candy/

import sys

# O(n) time solution
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):           
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(len(ratings) - 1)):           
            if ratings[i + 1] < ratings[i] and candy[i + 1] >= candy[i]:
                candy[i] = candy[i + 1] + 1
        return sum(candy)