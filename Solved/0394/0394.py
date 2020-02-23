# Problem No.: 394
# Solver:      Jinmin Goh
# Date:        20200224
# URL: https://leetcode.com/problems/decode-string/

import sys

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        stack = [""]
        integer = "1234567890"
        i = 0
        temp = None
        while i < len(s):
            #print(i, stack, temp)
            if s[i] in integer:
                if temp:
                    stack.append(s[temp:i])
                num = ""
                num += s[i]
                while s[i + 1] in integer:
                    num += s[i + 1]
                    i += 1
                temp = i + 2
                stack.append(num)
                i += 2
            elif s[i] == "]":
                if temp:
                    stack.append(s[temp:i])
                #print(stack)
                string = stack.pop()
                num = int(stack.pop())
                string = string * num
                newStr = stack.pop()
                stack.append(newStr + string)
                i += 1
                temp = None
            else:
                if not stack[-1] or stack[-1][0] not in integer:
                    string = stack.pop()
                    string += s[i]
                    stack.append(string)
                i += 1
        return stack.pop()   