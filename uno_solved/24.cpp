#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
    
};

ListNode* swapPairs(ListNode* head) {
    ListNode* head_store = head;
    ListNode* temp;
    ListNode* prev = NULL;
    while (head != NULL)
    {
        temp = head->next;
        if (temp == NULL)
            break;
        head->next = temp->next;
        temp->next = head;
        if (prev == NULL)
            head_store = temp;
        else
            prev->next = temp;
        prev = head;
        head = head->next;
    }
    return head_store;
}