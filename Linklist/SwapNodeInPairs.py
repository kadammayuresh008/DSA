
# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head):
            ptr=head
            while(ptr!=None and ptr.next!=None):
                # temp=ptr.next
                # ptr.next=ptr.next.next
                # temp.next=ptr
                ptr.val,ptr.next.val=ptr.next.val,ptr.val
                ptr=ptr.next.next
            return head
        