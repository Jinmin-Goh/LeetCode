/*#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    int veclen = strs.size();
    if (veclen == 0)
        return "";
    int len = (strs[0]).length();
    char c;
    int i;
    for (i = 0; i < len; i++)
    {
        c = strs[0][i];
        for (int j = 0; j < veclen; j++)
        {
            if (c != strs[j][i])
                goto fail;
        }
    }
fail:
    return (strs[0]).substr(0, i);
}

*/