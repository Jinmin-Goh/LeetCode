/*
//n^2 log n algorithm.
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int len = nums.size();
    int pos;
    vector<vector<int>> ans;
    vector<int>::iterator up;
    for (int i = 0; i < len - 1; i++)
    {
        if (nums[i] == nums[i + 1])
        {
            int j;
            for (j = 0; j < len; j++)
            {
                if (j == i || j == i + 1)
                    continue;
                if (-(nums[i] + nums[i + 1]) == nums[j])
                    break;
            }
            if (j < len)
            {
                vector<int> a;
                a.push_back(nums[i]);
                a.push_back(nums[i + 1]);
                a.push_back(nums[j]);
                ans.push_back(a);
            }
            while (i < len - 1 && nums[i] == nums[i + 1])
                i++;
        }
    }
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    len = nums.size();
    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            up = lower_bound(nums.begin(), nums.end(), -(nums[i] + nums[j]));
            pos = up - nums.begin();
            if (j < pos && pos < len && -(nums[i] + nums[j]) == nums[pos])
            {
                vector<int> a;
                a.push_back(nums[i]);
                a.push_back(nums[j]);
                a.push_back(nums[pos]);
                ans.push_back(a);
            }
        }
    }
    return ans;
}
*/