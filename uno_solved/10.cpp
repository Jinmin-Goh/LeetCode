#include<iostream>
#include<algorithm>

using namespace std;

bool ans = false;
bool term = false;
inline int read_p(char c)
{
    if ('a' <= c && c <= 'z')
        return 0;
    else if (c == '.')
        return 1;
    else if (c == '*')
        return 2;
    return -1;
}
void isMatch_aux(const string& s, int j, const string& p, int i)
{
    if (ans)
        return;

    if (p[i] == 0)
    {
        if (s[j] == 0)
        {
            ans = true;
            return;
        }
        return;
    }
    int val, next_val;
    val = read_p(p[i]);
    next_val = read_p(p[i + 1]);
    if (s[j] == 0)
    {
        if (next_val == 2)
            isMatch_aux(s, j, p, i + 2);
        return;
    }
    if (next_val == 2)
    {
        isMatch_aux(s, j, p, i + 2);
        switch (val)
        {
        case 0: if (p[i] != s[j]) return; break;
        case 1: if (s[j] == 0) return; break;
        default: return;
        }
        isMatch_aux(s, j + 1, p, i);
        return;
    }
    switch (val)
    {
    case 0: if (p[i] != s[j]) return; else isMatch_aux(s, j + 1, p, i + 1); break;
    case 1: if (s[j] == 0) return; else isMatch_aux(s, j + 1, p, i + 1); break;
    default: return;
    }
}
bool isMatch(string s, string p) {
    bool dot_state = false;
    bool star_state = false;

    isMatch_aux(s, 0, p, 0);
    return ans;
}
int main()
{
    cout<<isMatch("ab", ".*c");
}