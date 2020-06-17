# Problem No.: 468
# Solver:      Jinmin Goh
# Date:        20200617
# URL: https://leetcode.com/problems/validate-ip-address/

import sys

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ("." in IP and ":" in IP) or ("." not in IP and ":" not in IP):
            return "Neither"
        
        # check IPv4
        if "." in IP:
            cnt = 0
            dotPos = []
            for i in range(len(IP)):
                if IP[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                    return "Neither"
                if IP[i] == ".":
                    cnt += 1
                    dotPos.append(i)
            if cnt != 3:
                return "Neither"
            # no leading 0s
            if IP[0] == "0" or (IP[dotPos[0] + 1] == "0" and IP[dotPos[0] + 2] != ".") or (IP[dotPos[1] + 1] == "0" and IP[dotPos[1] + 2] != ".") or dotPos[2] == len(IP) - 1 or (IP[dotPos[2] + 1] == "0" and dotPos[2] + 1 != len(IP) - 1):
                return "Neither"
            if dotPos[0] > 3 or dotPos[0] == 0 or dotPos[1] - dotPos[0] > 4 or dotPos[2] - dotPos[1] > 4 or len(IP) - dotPos[2] > 4 or dotPos[1] - dotPos[0] < 2 or dotPos[2] - dotPos[1] < 2 or len(IP) - dotPos[2] < 2:
                return "Neither"
            num1 = int(IP[:dotPos[0]])
            num2 = int(IP[dotPos[0] + 1:dotPos[1]])
            num3 = int(IP[dotPos[1] + 1:dotPos[2]])
            num4 = int(IP[dotPos[2] + 1:])
            if num1 > 255 or num2 > 255 or num3 > 255 or num4 > 255:
                return "Neither"
            return "IPv4"
        
        # check IPv6
        if ":" in IP:
            cnt = 0
            dotPos = []
            for i in range(len(IP)):
                if IP[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F", ":"]:
                    return "Neither"
                if IP[i] == ":":
                    cnt += 1
                    dotPos.append(i)
            #print("check")
            if cnt != 7:
                return "Neither"
            
            if dotPos[0] > 4 or dotPos[1] - dotPos[0] > 5 or dotPos[2] - dotPos[1] > 5 or dotPos[3] - dotPos[2] > 5 or dotPos[4] - dotPos[3] > 5 or dotPos[5] - dotPos[4] > 5 or dotPos[6] - dotPos[5] > 5 or len(IP) - dotPos[6] > 5 or dotPos[0] == 0 or dotPos[1] - dotPos[0] < 2 or dotPos[2] - dotPos[1] < 2 or dotPos[3] - dotPos[2] < 2 or dotPos[4] - dotPos[3] < 2 or dotPos[5] - dotPos[4] < 2 or dotPos[6] - dotPos[5] < 2 or len(IP) - dotPos[6] < 2:
                return "Neither"

            return "IPv6"
        