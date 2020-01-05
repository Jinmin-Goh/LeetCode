//nlog n algorithm

#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

vector<int> my;
int bsort(vector<int>& nums, int target)
{
	int beg = 0;
	int end = nums.size() - 1;
	int mid, temp;
	while (beg <= end)
	{
		mid = (beg + end) / 2;
		temp = nums[mid];
		if (temp == target)
			return mid;
		else if (temp < target)
			beg = mid + 1;
		else if (temp > target)
			end = mid - 1;
	}
	return -1;
}
vector<int> twoSum(vector<int>& nums, int target) {
	int s = nums.size();
	vector<int> mynums;
	for (int i = 0; i < s; i++)
	{
		mynums.push_back(nums[i]);
	}
	sort(&nums[0], &nums[nums.size() - 1]);

	int res;
	vector<int> ans;
	int tempans1 = -1;
	int tempans2 = -1;
	for (int i = 0; i < s; i++)
	{
		res = bsort(nums, target - nums[i]);
		if (res != -1 && res != i)
		{
			for (int j = 0; j < s; j++)
			{
				if (mynums[j] == nums[i] && tempans1 == -1)
					tempans1 = j;
				else if (mynums[j] == nums[res] && tempans2 == -1)
					tempans2 = j;
			}

			nums.clear();
			if (tempans1 < tempans2)
			{
				nums.push_back(tempans1);
				nums.push_back(tempans2);
			}
			else
			{
				nums.push_back(tempans2);
				nums.push_back(tempans1);
			}
			return nums;
		}
	}
	return nums;
}

int main()
{
	int temp;
	for (int i = 0; i < 5; i++)
	{
		cin >> temp;
		my.push_back(temp);
	}
	twoSum(my, 4);
	for (int i = 0; i < my.size(); i++)
	{
		cout << my[i] << endl;
	}
}
