# Problem No.: 131
# Solver:      Jinmin Goh
# Date:        20200121
# URL: https://leetcode.com/problems/palindrome-partitioning/

import sys

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # solve with DP
        if not s:
            return [[]]
        
        self.ans = [] # holds every stage's answer
        # find answer in every s[:i + 1] and record it
        for i in range(len(s)):
            self.findFunc(s[:i + 1])
        return self.ans[-1]

    def findFunc(self, s: str) -> None:
        if len(s) == 1:
            self.ans.append([[s]])
            return
        self.ans.append([])
        for i in self.ans[-2]:
            self.ans[-1].append(i[:])
        for i in self.ans[-1]:
            i.append(s[-1])
        
        for i in range(len(s) - 1):
            flag = True
            if s[-1] == s[i]:
                for j in range((len(s) - i) // 2):
                    if s[i + j] != s[len(s) - j - 1]:
                        flag = False
                        break
            else:
                flag = False
            if flag:
                tempstr = s[i:]
                tempList = []
                tempList.append([tempstr])
                for j in range(len(tempstr) // 2):
                    if len(tempstr) - j - 2 < j + 1:
                        leftTemp = []
                        rightTemp = []
                        for k in range(j + 1):
                            leftTemp = leftTemp + [tempstr[k]]
                            rightTemp = [tempstr[-k - 1]] + rightTemp
                        tempList.append(leftTemp + rightTemp)
                    else:
                        leftTemp = []
                        rightTemp = []
                        for k in range(j + 1):
                            leftTemp = leftTemp + [tempstr[k]]
                            rightTemp = [tempstr[-k - 1]] + rightTemp
                        tempList.append(leftTemp + [tempstr[j + 1:-j - 1]] + rightTemp)
                for j in tempList:
                    if i == 0:
                        if j[:] not in self.ans[-1]:
                            self.ans[-1].append(j[:])
                    else:
                        for k in self.ans[i - 1]:
                            if k + j not in self.ans[-1]:
                                self.ans[-1].append(k + j)
                    
            