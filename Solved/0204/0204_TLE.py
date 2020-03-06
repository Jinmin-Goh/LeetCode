# Problem No.: 204
# Solver:      Jinmin Goh
# Date:        20200306
# URL: https://leetcode.com/problems/count-primes/

import sys

# 19/20 passed and TLE

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primeList = []
        for i in range(2, n):
            if not primeList:
                primeList.append(i)
                continue
            primeFlag = True
            for prime in primeList:
                if i % prime == 0:
                    primeFlag = False
                    break
                if prime > int(i ** 0.5):
                    break
            if primeFlag:
                primeList.append(i)
            #print(primeList)
        return len(primeList)