# https://leetcode.com/problems/binary-tree-right-side-view/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if(root):
            queue=[]
            queue.append(root)
            ans=[]
            while(queue):
                size=len(queue)
                for i in range(0,size):
                    x=queue.pop(0)
                    if(i==size-1):
                        ans.append(x.val)
                    if(x.left):
                        queue.append(x.left)
                    if(x.right):
                        queue.append(x.right)
            return ans
        