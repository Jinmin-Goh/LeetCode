# Problem No.: 621
# Solver:      Jinmin Goh
# Date:        20200229
# URL: https://leetcode.com/problems/task-scheduler/

import sys

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 or len(tasks) == 1:
            return len(tasks)
        wordDict = {}
        maxVal = 0
        for i in tasks:
            if i not in wordDict:
                wordDict[i] = 1
            else: 
                wordDict[i] += 1
        ans = 0
        while wordDict:
            if len(wordDict) >= n + 1:
                delList = []
                valList = []
                maxVal = 0
                ans += n + 1
                for i in wordDict:
                    valList.append((wordDict[i], i))
                valList.sort()
                for i in range(n + 1):
                    wordDict[valList[-i - 1][1]] -= 1
                    if wordDict[valList[-i - 1][1]] == 0:
                        delList.append(valList[-i - 1][1])
                for i in delList:
                    del wordDict[i]
                for i in wordDict:
                    maxVal = max(maxVal, wordDict[i])
                if maxVal == 1:
                    ans += len(wordDict)
                    break
            else:
                delList = []
                maxVal = 0
                ans += n + 1
                for i in wordDict:
                    wordDict[i] -= 1
                    maxVal = max(maxVal, wordDict[i])
                    if wordDict[i] == 0:
                        delList.append(i)
                #print(ans)
                for i in delList:
                    del wordDict[i]
                if maxVal == 1:
                    ans += len(wordDict)
                    print(ans)
                    break
                if not wordDict:
                    ans -= 1
        return ans