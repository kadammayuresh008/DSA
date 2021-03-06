
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head):
            odd=head
            even=head.next
            evenHead=even
            while(even!=None and even.next!=None):
                odd.next=even.next
                odd=odd.next
                even.next=odd.next
                even=even.next
            odd.next=evenHead
            return head