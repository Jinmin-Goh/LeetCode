# Problem No.: 68
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/text-justification/

import sys

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # empty slots on the left will be assigned more spaces
        i = 0
        temp_cnt = 0
        temp_list = []
        ans = []
        while i < len(words):
            if temp_cnt + len(words[i]) > maxWidth:
                if len(temp_list) > 1:
                    word_len = 0
                    for word in temp_list:
                        word_len += len(word)
                    common_cnt = (maxWidth - word_len) // (len(temp_list) - 1)
                    remainder = (maxWidth - word_len) % (len(temp_list) - 1)
                    temp_ans = ""
                    for j in range(len(temp_list) - 1):
                        temp_ans += temp_list[j] + " " * common_cnt
                        if remainder:
                            temp_ans += " "
                            remainder -= 1
                    temp_ans += temp_list[-1]
                # if only one word in sequence
                else:
                    temp_ans = temp_list[0]
                    while len(temp_ans) < maxWidth:
                        temp_ans += " "
                ans.append(temp_ans)
                temp_cnt = 0
                temp_list = []
            temp_list.append(words[i])
            temp_cnt += len(words[i]) + 1
            i += 1
            
        # make last line
        if temp_list:
            temp_ans = ""
            for i in range(len(temp_list) - 1):
                temp_ans += temp_list[i] + " "
            temp_ans += temp_list[-1]
            while len(temp_ans) < maxWidth:
                temp_ans += " "
            ans.append(temp_ans)
        return ans