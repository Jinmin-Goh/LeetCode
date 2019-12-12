# Problem No.: 30
# Solver:      Jinmin Goh
# Date:        20191212
# URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/

import sys

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words or len(s) < len(words):
            return []
        ans = []
        pointer_front = 0
        pointer_rear = 0
        word_len = len(words[0])
        temp_list = words[:]
        while pointer_front + word_len - 1 < len(s):
            temp_list = words[:]
            if s[pointer_front:pointer_front + word_len] in words:
                temp_list.remove(s[pointer_front:pointer_front + word_len])
                pointer_rear = pointer_front + word_len
                while pointer_rear + word_len - 1 < len(s) and temp_list:
                    if s[pointer_rear:pointer_rear + word_len] in temp_list:
                        temp_list.remove(s[pointer_rear:pointer_rear + word_len])
                        pointer_rear += word_len
                    else:
                        break
                if not temp_list:
                    ans.append(pointer_front)
                    pointer_front += 1
                    continue
                else:
                    pointer_front += 1
            else:
                pointer_front += 1
        return ans
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        