#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int lengthOfLongestSubstring(string s) {
    if (s.length() == 0)
        return 0;
    int len = s.length();
    int dp = len;
    int j;
    int m = 1;

    char c1, c2;
    for (int i = len - 2; i >= 0; i--)
    {
        c1 = s[i];
        int j;
        for (j = i + 1; j < dp; j++)
        {
            if (s[j] == c1)
                break;
        }
        dp = j;
        m = max(m, dp - i);
    }
    return m;
}

int main()
{
    cout << lengthOfLongestSubstring("a");
}