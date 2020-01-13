/*#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
    long long a[10];
    int reverse(int x) {
        int i = 0;
        bool sign = false;
        if (x == -2147483648)
            return 0;
        if (x < 0)
        {
            sign = true;
            x = -x;
        }
        if (x < 0)
            return 0;

        while (x != 0)
        {
            a[i] = x % 10;
            x /= 10;
            i++;
        }
        if (i == 10 && a[0] > 2)
            return 0;
        long long mul = 1;
        for(int j = i - 1; j >= 0; j--)
        {
            x += (a[j] * mul);
            mul *= 10;
        }
        if (x < 0)
            return 0;
        if (sign == true)
            return -x;
        return x;
    }
int main()
{
    cout << reverse(1534236469);
}
*/