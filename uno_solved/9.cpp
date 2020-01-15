#include<iostream>
#include<algorithm>

using namespace std;

bool isPalindrome(int x) {
    if (x < 0)
        return false;
    if (x == 0)
        return true;
    long long x_origin = x;
    long long i = 1;
    long long mul = 1;
    while (x != 0)
    {
        x /= 10;
        i *= 10;
    }
    i /= 10;

    while (i > mul)
    {
        if (((x_origin / i) % 10) != ((x_origin / mul) % 10))
            return false;
        i /= 10;
        mul *= 10;
    }
    return true;
}
int main()
{
    cout << isPalindrome(12321);
}