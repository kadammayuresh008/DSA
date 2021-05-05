# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None):
            return head
        if(head):
            ptr=head
            dict1={}
            while(ptr):
                if(ptr.val not in dict1):
                    dict1[ptr.val]=1
                else:
                    dict1[ptr.val]+=1
                ptr=ptr.next
            prev=head
            ptr2=head.next
            while(ptr2):
                if(dict1[ptr2.val]>1):
                    prev.next=ptr2.next
                    ptr2=prev.next
                else:
                    prev=ptr2
                    ptr2=ptr2.next
            if(dict1[head.val]>1):
                head=head.next
            return head