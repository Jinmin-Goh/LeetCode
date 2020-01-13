/*#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

char** dp;
bool check_string(string s, int i, int j)
{
    if (s[i] != s[j])
        goto fail;
    else if (s[i] == s[j] && j - i <= 1)
        goto success;
    if (dp[i + 1][j - 1] == 2)
        goto success;
    else if (dp[i + 1][j - 1] == 1)
        goto fail;
    for (int k = 1; k <= (j - i) / 2; k++)
    {
        if (s[i + k] != s[j - k])
            goto fail;
    }
    goto success;
fail: dp[i][j] = 1; return false;
success:
    for (int k = 0; k <= (j - i) / 2; k++)
    {
        dp[i + k][j - k] = 2;
    }
    return true;
}
string longestPalindrome(string s) {

    size_t s_length = s.length();
    if (s_length == 0)
        return s;
    dp = new char* [s_length + 1];
    for (int i = 0; i < s_length + 1; i++)
    {
        dp[i] = new char[s_length + 1]();
    }
    size_t token = 0;
    size_t len = 1;

    for (int i = 0; i < s_length; i++)
    {
        for (int j = i; j < s_length; j++)
        {
            if (len < j + 1 - i && check_string(s, i, j))
            {
                token = i;
                len = j + 1 - i;
            }
        }
    }
    return s.substr(token, len);
}
int main()
{
    string s = "iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz";
    cout<<longestPalindrome(s);
    return 0;
}
*/