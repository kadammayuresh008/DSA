


# https://leetcode.com/problems/rotate-list/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    if(head==NULL )
    {
        return NULL;
    }
    else{
    struct ListNode* ptr=head,*start=NULL,*x=head;
    int count=0;
    while(ptr!=NULL)
    {
        count++;
        ptr=ptr->next;
    }
    int i=0;
    int m=k%count;
    if(m==0){
        return head;
    }
    else{
    ptr=head;
    while(i<count-(k%count)-1){
        ptr=ptr->next;
        i++;
    }
    start=ptr->next;
    ptr->next=NULL;
    head=start;
    while(start->next!=NULL)
    {
        start=start->next;
    }
    start->next=x;
    return head;
    }
    }
}