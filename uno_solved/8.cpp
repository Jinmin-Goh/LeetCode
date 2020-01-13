/*#include<iostream>
#include<algorithm>

using namespace std;

long long a[10];
int check_validity(char c)
{
    if (0 <= c - '0' && c - '0' <= 9)
        return 1;
    else if (c == '-')
        return 3;
    else if (c == '+')
        return 4;
    else if (c == ' ')
        return 2;
    else
        return 0;
}
int myAtoi(string str) {
    bool sign = false;
    bool sign_check = false;
    int i = 0;
    if (str.length() == 0 || check_validity(str[0]) == 0)
        return 0;
    while (str[i] != 0)
    {
        switch (check_validity(str[i]))
        {
        case 0: return 0;
        case 3: if (sign_check == false)
            sign = true;
              else
            return 0;
            sign_check = true;
            break;
        case 4: if (sign_check != false)
            return 0;
            sign_check = true;
            break;
        case 1: goto escape;
        default: if (sign_check) return 0; else break;
        }
        i++;
    }
escape:
    if (str[i] == 0)
        return 0;
    int j = 0;
    int sum = 0;
    long long mul = 1;
    while (str[i] == '0')
        i++;
    if (str[i] == 0)
        return sum;
    while (check_validity(str[j + i]) == 1 && j < 10)
    {
        a[j] = str[i + j] - '0';
        j++;
    }
    if (j == 10 && str[9 + i] != 0 && check_validity(str[j + i]) == 1)
    {
        if (sign)
            return -INT_MAX - 1;
        return INT_MAX;
    }
    if (j == 10 && a[0] > 2)
    {
        if (sign)
            return -INT_MAX - 1;
        return INT_MAX;
    }
    for (int k = j - 1; k >= 0; k--)
    {
        sum += (a[k] * mul);
        mul *= 10;
    }
    if (!sign && sum < 0)
        return INT_MAX;
    else if (sign && sum < 0)
        return -INT_MAX - 1;
    else if (sum == 0)
        return 0;
    if (sign)
        return -sum;
    else
        return sum;
}
int main()
{
    cout << myAtoi("-2147483648");
}
*/