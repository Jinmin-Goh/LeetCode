# Problem No.: ???
# Solver:      Jinmin Goh
# Date:        20200414
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

import sys

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for i in shift:
            if i[0] == 0:
                move -= i[1]
            else:
                move += i[1]
        move = move % len(s)
        ans = s[-move:] + s[:-move]
        return ans