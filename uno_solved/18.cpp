/*#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<vector<int>> fourSum(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> ans;
    int len = nums.size();
    int lpivot;
    int rpivot;
    int temp1, temp2;
    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len - 2; j++)
        {
            lpivot = j + 1;
            rpivot = len - 1;
            temp1 = nums[i] + nums[j];
            while (lpivot < rpivot)
            {
                if (lpivot == i || lpivot == j)
                {
                    lpivot++;
                    continue;
                }
                else if (rpivot == i || rpivot == j)
                {
                    rpivot--;
                    continue;
                }
                temp2 = temp1 + nums[lpivot] + nums[rpivot];
                if (temp2 < target)
                    lpivot++;
                else if (temp2 > target)
                    rpivot--;
                else
                {
                    vector<int> t;
                    t.push_back(nums[i]);
                    t.push_back(nums[j]);
                    t.push_back(nums[lpivot]);
                    t.push_back(nums[rpivot]);
                    ans.push_back(t);
                    while (rpivot > 0 && nums[rpivot] == nums[rpivot - 1])
                        rpivot--;
                    rpivot--;
                }
            }

            while (j < len - 1 && nums[j] == nums[j + 1])
                j++;
        }
        while (i < len - 1 && nums[i] == nums[i + 1])
            i++;
    }
    return ans;
}
*/