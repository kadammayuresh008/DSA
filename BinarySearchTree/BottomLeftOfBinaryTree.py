# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if(root):
            queue=[]
            queue.append(root)
            while(queue):
                x=len(queue)
                li=[]
                for i in range(0,x):
                    ans=queue.pop(0)
                    li.append(ans.val)
                    if(ans.left):
                        queue.append(ans.left)
                    if(ans.right):
                        queue.append(ans.right)
        return li[0]
                    
        