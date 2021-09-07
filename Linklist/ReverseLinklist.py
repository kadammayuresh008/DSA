# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head):
            curr=head
            prev=None
            while(curr):
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
            head=prev
            return head
        