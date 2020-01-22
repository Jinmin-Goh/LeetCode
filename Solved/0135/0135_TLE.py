# Problem No.: 135
# Solver:      Jinmin Goh
# Date:        20200122
# URL: https://leetcode.com/problems/candy/

import sys

# 44/48 passed and TLE solution
# time: O(n^2)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            elif ratings[i] < ratings[i - 1]:
                if candy[i - 1] == 1:
                    temp = i - 1
                    candy[temp] += 1
                    while temp > 0 and ratings[temp] < ratings[temp - 1] and candy[temp] >= candy[temp - 1]:
                        candy[temp - 1] += 1
                        temp -= 1
        return sum(candy)