//NOT COMPELTE CODE.
/*#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int num1size = nums1.size() - 1;
    int num2size = nums2.size() - 1;
    if (num1size > num2size)
    {
        return findMedianSortedArrays(nums2, nums1);
    }
    int target = (num1size + num2size) / 2;
    int beg = 0;
    int end = num1size;
    int pivot1;
    int pivot2;
    while (pivot1 > 0 && pivot1 < num1size && beg <= end)
    {
        pivot1 = (beg + end) / 2;
        pivot2 = target - pivot1;
        if (nums1[pivot1 + 1] >= nums2[pivot2] && nums2[pivot2 - 1] <= nums1[pivot1] && 
            nums2[pivot2 + 1] >= nums1[pivot1] && nums1[pivot1 - 1] <= nums2[pivot2])
        {
            goto nums1end;
        }
        else if (nums1[pivot1] > nums2[pivot2])
        {
            end = pivot1 - 1;
        }
        else
        {
            beg = pivot1 + 1;
        }
    }
    if (nums1[pivot1] >= nums2[pivot2])
    {
        if (pivot2 < num2size && nums2[pivot2 + 1] <= nums1[pivot1])
        {
            if ((num1size + num2size) % 2 == 1)
                return nums2[pivot2 + 1];
            return (((double)nums2[pivot2] + nums2[pivot2 + 1]) / 2);
        }
        goto nums1end;
    }
    else
    {
        if (pivot2 > 0 && nums2[pivot2 - 1] >= nums1[pivot1])
        {
            if ((num1size + num2size) % 2 == 1)
                return nums2[pivot2];
            return (((double)nums2[pivot2 - 1] + nums2[pivot2]) / 2);
        }
        goto nums1end;
    }
nums1end:
    if ((num1size + num2size) % 2 == 1)
        return max (nums1[pivot1], nums2[pivot2]);
    return (((double)nums1[pivot1] + nums2[pivot2]) / 2);
}
int main() {
    vector<int> a;
    vector<int> b;
    a.push_back(1);
    a.push_back(3);
    a.push_back(5);
    a.push_back(5);
    a.push_back(7);
    a.push_back(8);
    a.push_back(9);
    a.push_back(10);
    b.push_back(2);
    b.push_back(4);
    b.push_back(6);
    b.push_back(6);
    b.push_back(7);
    b.push_back(9);
    cout<<findMedianSortedArrays(a, b);
}
*/