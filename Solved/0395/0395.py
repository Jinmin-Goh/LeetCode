# Problem No.: 395
# Solver:      Jinmin Goh
# Date:        20200401
# URL: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

import sys

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        wordDict = {}
        ans = 0
        validSet = set()
        for i in s:
            if i not in wordDict:
                wordDict[i] = 1
            else:
                wordDict[i] += 1
            if wordDict[i] >= k:
                validSet.add(i)
        ans = 0
        pFront = 0
        pRear = 0
        tempDict = {}
        while pRear < len(s) and pFront < len(s):
            if s[pFront] not in validSet:
                pFront += 1
                pRear += 1
                continue
            elif s[pRear] not in validSet:
                flag = True
                while flag and pFront < pRear:
                    tempMax = 0
                    tempMin = len(s)
                    for i in tempDict:
                        tempMin = min(tempDict[i], tempMin)
                        tempMax = max(tempDict[i], tempMax)
                    if tempMax < k:
                        pFront = pRear
                        tempDict = {}
                        break
                    if tempMin >= k:
                        ans = max(ans, pRear - pFront)
                        pFront = pRear
                        flag = False
                    else:
                        tempDict[s[pFront]] -= 1
                        if tempDict[s[pFront]] == 0:
                            del tempDict[s[pFront]]
                        pFront += 1
            else:
                if s[pRear] not in tempDict:
                    tempDict[s[pRear]] = 1
                else:
                    tempDict[s[pRear]] += 1
                pRear += 1
                temptempDict = {}
                for i in tempDict:
                    temptempDict[i] = tempDict[i]
                temppFront = pFront
                temppRear = pRear
                flag = True
                while flag and temptempDict and temppFront < len(s) and temppRear < len(s):
                    tempMax = 0
                    tempMin = len(s)
                    for i in temptempDict:
                        tempMin = min(temptempDict[i], tempMin)
                        tempMax = max(temptempDict[i], tempMax)
                    if tempMax < k:
                        temppFront = temppRear
                        temptempDict = {}
                        break
                    if tempMin >= k:
                        ans = max(ans, temppRear - temppFront)
                        temppFront = temppRear
                        flag = False
                    else:
                        temptempDict[s[temppFront]] -= 1
                        if temptempDict[s[temppFront]] == 0:
                            del temptempDict[s[temppFront]]
                        temppFront += 1
        if pFront < len(s):
            flag = True
            while flag and tempDict:
                tempMax = 0
                tempMin = len(s)
                for i in tempDict:
                    tempMin = min(tempDict[i], tempMin)
                    tempMax = max(tempDict[i], tempMax)
                if tempMax < k:
                    break
                if tempMin >= k:
                    ans = max(ans, pRear - pFront)
                    pFront = pRear
                    flag = False
                else:
                    tempDict[s[pFront]] -= 1
                    if tempDict[s[pFront]] == 0:
                        del tempDict[s[pFront]]
                    pFront += 1
        return ans