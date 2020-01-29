#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) { }
};

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
{
	if (l1 == NULL)
		return l2;
	else if (l2 == NULL)
		return l1;
	if (l1->val > l2->val)
		return mergeTwoLists(l2, l1);
	ListNode* head = l1;
	ListNode* prev = NULL;
	ListNode* temp;
	while (l1 != NULL && l2 != NULL)
	{
		if (l1->val <= l2->val)
		{
			prev = l1;
			l1 = l1->next;
		}
		else
		{
			temp = new ListNode(l2->val);
			temp->next = prev->next;
			prev->next = temp;
			prev = prev->next;
			l2 = l2->next;
		}
	}
	if (l1 == NULL)
	{
		while (l2 != NULL)
		{
			temp = new ListNode(l2->val);
			temp->next = NULL;
			prev->next = temp;
			prev = prev->next;
			l2 = l2->next;
		}
	}
	return head;
}