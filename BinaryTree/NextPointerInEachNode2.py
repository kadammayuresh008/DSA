# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
         if(root):
            queue=[]
            queue.append(root)
            while(queue):
                size=len(queue)
                for j in range(0,size):
                    x=queue.pop(0)
                    if(j==size-1):
                        x.next=None
                    else:
                        x.next=queue[0]
                    if(x.left):
                        queue.append(x.left)
                    if(x.right):
                        queue.append(x.right)
            return root
        