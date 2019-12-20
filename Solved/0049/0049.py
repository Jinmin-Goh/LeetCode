# Problem No.: 49
# Solver:      Jinmin Goh
# Date:        20191220
# URL: https://leetcode.com/problems/group-anagrams/

import sys

class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        hash_table = None
        for string in strs:
            temp = []
            for i in string:
                temp.append(i)
            temp.sort()
            if not hash_table:
                hash_table = {tuple(temp):[string]}
            else:
                if tuple(temp) in hash_table:
                    hash_table[tuple(temp)] += [string]
                else: 
                    hash_table[tuple(temp)] = [string]
        return list(hash_table.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        