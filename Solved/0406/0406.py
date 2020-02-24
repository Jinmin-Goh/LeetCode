# Problem No.: 406
# Solver:      Jinmin Goh
# Date:        20200224
# URL: https://leetcode.com/problems/queue-reconstruction-by-height/

import sys

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort()
        temp = people[-1][0]
        i = len(people) - 1
        while i >= 0 and people[i][0] == temp:
            i -= 1
        while i >= 0:
            #print(i, people)
            cnt = people[i][1]
            pos = i
            temp = people[i][0]
            tempPos = i
            while people[tempPos][0] == temp:
                tempPos -= 1
                cnt -= 1
            cnt += 1
            while cnt > 0:
                people[pos], people[pos + 1] = people[pos + 1], people[pos]
                cnt -= 1
                pos += 1
            i -= 1
        return people