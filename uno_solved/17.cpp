/*#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

void aux_ftn(vector<string>& vecstr, string& digits, int depth)
{
    if (digits.length() <= depth)
        return;

    int veclen = vecstr.size();
    for (int i = 0; i < veclen; i++)
    {
        switch (digits[depth] - '0')
        {
        case 2: vecstr.push_back((vecstr[i] + "b"));
            vecstr.push_back((vecstr[i] + "c"));
            vecstr[i] += "a";
            break;
        case 3: vecstr.push_back((vecstr[i] + "e")); vecstr.push_back((vecstr[i] + "f")); vecstr[i] += "d"; break;
        case 4: vecstr.push_back((vecstr[i] + "h")); vecstr.push_back((vecstr[i] + "i")); vecstr[i] += "g"; break;
        case 5: vecstr.push_back((vecstr[i] + "k")); vecstr.push_back((vecstr[i] + "l")); vecstr[i] += "j"; break;
        case 6: vecstr.push_back((vecstr[i] + "n")); vecstr.push_back((vecstr[i] + "o")); vecstr[i] += "m"; break;
        case 7: vecstr.push_back((vecstr[i] + "q")); vecstr.push_back((vecstr[i] + "r")); vecstr.push_back((vecstr[i] + "s")); vecstr[i] += "p"; break;
        case 8: vecstr.push_back((vecstr[i] + "u")); vecstr.push_back((vecstr[i] + "v")); vecstr[i] += "t"; break;
        case 9: vecstr.push_back((vecstr[i] + "x")); vecstr.push_back((vecstr[i] + "y")); vecstr.push_back((vecstr[i] + "z")); vecstr[i] += "w"; break;
        default: break;
        }
    }
    aux_ftn(vecstr, digits, depth + 1);
}
vector<string> letterCombinations(string digits) {
    vector<string> mystrvec;
    if (digits.length() == 0)
        return mystrvec;
    mystrvec.push_back("");
    aux_ftn(mystrvec, digits, 0);
    return mystrvec;
}
*/