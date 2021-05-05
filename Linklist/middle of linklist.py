https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if(head):
            slow=head
            fast=head
            start=head
            counter=0
            while(start!=None):
                counter+=1
                start=start.next
            if(counter%2==0):
                x=int(counter/2)
                while(x>0):
                    fast=fast.next
                    x-=1
                return fast
            else:
                x=int(counter/2)
                while(x>0):
                    slow=slow.next
                    x-=1
                return slow        