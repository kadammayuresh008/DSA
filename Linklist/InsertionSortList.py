
# https://leetcode.com/problems/insertion-sort-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head.next
        while(ptr!=None):
            curr=head
            while(curr!=ptr):
                if(curr.val>ptr.val):
                    ptr.val,curr.val=curr.val,ptr.val
                curr=curr.next
            ptr=ptr.next
        return head
        