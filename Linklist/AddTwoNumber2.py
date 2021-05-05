


# https://leetcode.com/problems/add-two-numbers-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1=l1
        ptr2=l2
        count,count1=0,0
        num1,num2="",""
        while(ptr1 or ptr2):
            if(ptr1):
                count+=1
                num1+=str(ptr1.val)
                ptr1=ptr1.next
            if(ptr2):
                count1+=1
                num2+=str(ptr2.val)
                ptr2=ptr2.next
        num3=str(int(num1)+int(num2))
        new_node=ListNode(num3[0],None)
        ans1=new_node
        ans=ans1
        for i in range(1,len(num3)):
            new_node=ListNode(int(num3[i]),None)
            ans.next=new_node
            ans=ans.next
        return ans1