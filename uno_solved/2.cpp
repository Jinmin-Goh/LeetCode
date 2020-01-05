#include<iostream>
#include<algorithm>

using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int sum;
    int up = 0;
    ListNode* origin1 = l1;
    ListNode* origin2 = l2;
    ListNode* bef1;
    ListNode* bef2;
    while (l1 != NULL && l2 != NULL)
    {
        sum = l1->val + l2->val;
        l1->val = (sum + up) % 10;
        l2->val = (sum + up) % 10;
        up = (sum + up) / 10;
        bef1 = l1;
        bef2 = l2;
        l1 = l1->next;
        l2 = l2->next;
    }
    if (l1 == NULL)
    {
        l1 = l2;
        bef1 = bef2;
        origin1 = origin2;
    }
    while (l1 != NULL)
    {
        sum = l1->val + up;
        l1->val = sum % 10;
        up = sum / 10;
        bef1 = l1;
        l1 = l1->next;
    }
    if (up == 1)
    {
        bef1->next = new ListNode(up);
    }
    return origin1;
}
