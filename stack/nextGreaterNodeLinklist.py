# https://leetcode.com/problems/next-greater-node-in-link



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        arr=[]
        ptr=head
        while(ptr!=None):
            arr.append(ptr.val)
            ptr=ptr.next
        stack=[]
        output_arr=[0]*len(arr)
        for i in range(0,len(arr)):
            while(stack!=[] and arr[stack[-1]]<arr[i]):
                output_arr[stack[-1]]=arr[i]
                stack.pop()
            stack.append(i)
        return output_arr
            