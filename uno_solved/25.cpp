/*#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}

};

ListNode* reverseList(ListNode* head, int k)
{
    ListNode* temp;
    ListNode* prev = head;
    while (k > 0)
    {
        temp = head->next;
        head->next = head->next->next;
        temp->next = prev;
        prev = temp;
        k--;
    }
    return head;
}
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode* prev = NULL;

    ListNode* head_store = head;
    ListNode* end = head;
    ListNode* temp = NULL;
    int j;
    int flag = false;
    if (k == 1)
        return head;

    while (1)
    {
        j = k - 1;
        end = head;
        while (end != NULL && j > 0)
        {
            end = end->next;
            j--;
        }
        if (end == NULL && j >= 0)
            return head_store;
        if (flag == false)
        {
            head_store = end;
            flag = true;
        }
        head = reverseList(head, k - 1);
        if (temp != NULL)
            temp->next = end;
        temp = head;
        head = head->next;
    }
}

int main()
{
    ListNode* head;
    head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next = new ListNode(6);
    reverseKGroup(head, 3);
    delete head->next->next->next->next->next;
    delete head->next->next->next->next;
    delete head->next->next->next;
    delete head->next->next;
    delete head->next;
    delete head;
}
*/