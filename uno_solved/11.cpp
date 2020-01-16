/*
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int maxArea(vector<int>& height) {
    int len = height.size();
    int i = 0;
    int j = len - 1;
    int m = 0;

    while (i < j)
    {
        len = min(height[i], height[j]);
        len = (j - i) * len;
        m = max(m, len);
        if (height[i] < height[j])
            i++;
        else
            j--;
    }
    return m;
}
*/