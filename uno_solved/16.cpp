/*#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int len = nums.size();
    int lpivot, rpivot;
    int temp;
    int diff = INT_MAX;
    int ans;
    for (int i = 0; i < len; i++)
    {
        lpivot = 0;
        rpivot = len - 1;
        while (lpivot < rpivot)
        {
            if (lpivot == i)
            {
                lpivot++;
                continue;
            }
            else if (rpivot == i)
            {
                rpivot--;
                continue;
            }

            temp = nums[i] + nums[lpivot] + nums[rpivot];

            if (abs(temp - target) < diff)
            {
                ans = temp;
                diff = abs(temp - target);
            }

            if (temp - target < 0)
                lpivot++;
            else
                rpivot--;
        }
        while (i < len - 1 && nums[i] == nums[i + 1])
            i++;
    }
    return ans;
}
*/