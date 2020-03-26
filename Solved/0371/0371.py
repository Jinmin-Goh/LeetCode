# Problem No.: 371
# Solver:      Jinmin Goh
# Date:        20200326
# URL: https://leetcode.com/problems/sum-of-two-integers/

import sys

# in 32-integer style

class Solution:
    def getSum(self, a: int, b: int) -> int:
        aFlag = bool(a & (1 << 31))
        bFlag = bool(b & (1 << 31))
        aLen = 0
        bLen = 0
        ans = 0
        # has different sign
        if aFlag ^ bFlag:
            if a == -2147483648 or b == -2147483648:
                return a | b
            carry = 0
            posBit = 1
            for i in range(32):
                if a % 2 and b % 2:
                    if carry:
                        ans += posBit
                    carry = 1
                elif (a % 2 ^ b % 2) and carry:
                    carry = 1
                elif not(a % 2 or b % 2) and not carry:
                    carry = 0
                else:
                    ans |= posBit
                    carry = 0
                a >>= 1
                b >>= 1
                posBit <<= 1
            if (a > b and aFlag) or (a < b and bFlag):
                ans |= 0x80000000
            ans = int(ans & 0xFFFFFFFF)
        # has same sign
        else:
            if aFlag:
                a = ~a
                if a & 1:
                    carry = 1
                    cnt = 1
                    while carry:
                        carry = int(bool(cnt & a))
                        a = a ^ cnt
                        cnt <<= 1
                else:
                    a |= 1
            if bFlag:
                b = ~b
                if b & 1:
                    carry = 1
                    cnt = 1
                    while carry:
                        carry = int(bool(cnt & b))
                        b = b ^ cnt
                        cnt <<= 1
                else:
                    b |= 1
            temp = a
            while temp:
                temp >>= 1
                aLen += 1
            temp = b
            while temp:
                temp >>= 1
                bLen += 1
            ans = 0
            upBit = 0
            posBit = 1
            for i in range(max(aLen, bLen) + 1):
                if a % 2 and b % 2:
                    if upBit:
                        ans += posBit
                    upBit = 1
                elif (a % 2 ^ b % 2) and upBit:
                    upBit = 1
                elif not(a % 2 or b % 2) and not upBit:
                    upBit = 0
                else:
                    ans += posBit
                    upBit = 0
                a >>= 1
                b >>= 1
                posBit <<= 1
            if aFlag:
                ans = ~ans
                if ans & 1:
                    carry = 1
                    cnt = 1
                    while carry:
                        carry = int(bool(cnt & ans))
                        ans = ans ^ cnt
                        cnt <<= 1
                else:
                    ans |= 1
            
        return ans