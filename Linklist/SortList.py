# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if(head):
            ptr=head
            list1=[]
            while(ptr!=None):
                list1.append(ptr.val)
                ptr=ptr.next
            list1.sort()
            ptr=head
            count=0
            while(ptr!=None):
                ptr.val=list1[count]
                count+=1
                ptr=ptr.next
            return head
            
        