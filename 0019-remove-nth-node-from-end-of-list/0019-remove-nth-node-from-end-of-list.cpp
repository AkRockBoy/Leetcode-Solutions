/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        ListNode* temp=head;
        int count=0;
        while (temp!=NULL)
        {
            count++;
            temp=temp->next;
        }
        if(count==n)
        {
          ListNode *temp1=head;
          head=head->next;
          delete temp1;
          return head;
        }
        int d=count-n;
        int c=1;
        temp=head;
        while(c!=d)
        {
            c++;
            temp=temp->next;
        }
        ListNode* temp1=temp->next;
        temp->next=temp1->next;
        delete temp1;
        return head;
    }
};