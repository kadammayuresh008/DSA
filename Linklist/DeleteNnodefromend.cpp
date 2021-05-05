// https://leetcode.com/problems/remove-nth-node-from-end-of-list/


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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
		if(head==nullptr ) return nullptr;
        ListNode* start=new ListNode(0,head);
        ListNode* stopatn=start,* stopatend=start;
        
        
        int i=0;
        while(stopatend!=nullptr)
        {
            
            if(i>n)
            {
                stopatn=stopatn->next;
            }
        
        stopatend=stopatend->next;
        i++;
        }
        
        stopatn->next=stopatn->next->next;
        return start->next;
    }
};