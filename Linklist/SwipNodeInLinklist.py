
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ptr=head
        ptr1=ptr
        for i in range(0,k-1):
            ptr=ptr.next
        first=ptr
        ptr=ptr.next
        while(ptr!=None):
            ptr=ptr.next
            ptr1=ptr1.next
        ptr1.val,first.val=first.val,ptr1.val
        return head
        