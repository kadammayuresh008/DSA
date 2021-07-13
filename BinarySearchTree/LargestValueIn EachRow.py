# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if(root):
            queue=[]
            visited=[]
            queue.append(root)
            visited.append(root)
            ans=[]
            while(queue):
                max1= -99999999999999999999999999999
                for i in range(0,len(queue)):
                    x=queue.pop(0)
                    if(x.val>max1):
                        max1=x.val
                    if(x.left):
                        queue.append(x.left)
                        visited.append(x.left)
                    if(x.right):
                        queue.append(x.right)
                        visited.append(x.right)
                ans.append(max1)
            return ans