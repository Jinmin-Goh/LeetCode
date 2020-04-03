# Problem No.: 174
# Solver:      Jinmin Goh
# Date:        20200403
# URL: https://leetcode.com/problems/dungeon-game/

import sys

# good solution: https://leetcode.com/problems/dungeon-game/discuss/52805/Best-solution-I-have-found-with-explanations
# used DP
# time: O(nm) / space: O(nm) for DP table

# for all position, knight must have at least max(1, 1 - min(down or right pos score)) to not die


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        nrow = len(dungeon)
        ncol = len(dungeon[0])
        dpTable = [[None] * ncol for _ in range(nrow)]
        for i in reversed(range(nrow)):
            for j in reversed(range(ncol)):
                if i == nrow - 1 and j == ncol - 1:
                    dpTable[i][j] = max(1, 1 - dungeon[i][j])
                elif i == nrow - 1:
                    dpTable[i][j] = max(1, dpTable[i][j + 1] - dungeon[i][j])
                elif j == ncol - 1:
                    dpTable[i][j] = max(1, dpTable[i + 1][j] - dungeon[i][j])
                else:
                    dpTable[i][j] = max(1, min(dpTable[i][j + 1], dpTable[i + 1][j]) - dungeon[i][j])
        return dpTable[0][0]