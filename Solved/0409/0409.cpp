// Problem No.: 409
// Solver:      Jinmin Goh
// Date:        20200816
// URL: https://leetcode.com/problems/longest-palindrome/

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int> wordMap;
        for(int i = 0; i < s.length(); i++) {
            if(wordMap.find(s[i]) == wordMap.end()) {
                wordMap[s[i]] = 1;
            }
            else {
                wordMap[s[i]]++;
            }
        }
        map<char, int>::iterator iter;
        bool flag = false;
        int ans = 0;
        for(iter = wordMap.begin(); iter != wordMap.end(); iter++) {
            if(iter->second % 2 && !flag) {
                flag = true;
                ans += iter->second;
            }
            else {
                ans += iter->second - iter->second % 2;
            }
        }
        return ans;
    }
};