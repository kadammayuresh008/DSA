# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list=[]
    def preorder(self,root):
        if(root):
            self.list.append(root)
            Solution.preorder(self,root.left)
            Solution.preorder(self,root.right)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root):
            head=root
            Solution.preorder(self,root)
            if(len(self.list)==1):
                x=self.list.pop(0)
                head=x 
                return head
            else:
                while(self.list):
                    x=self.list.pop(0)
                    head.left=None
                    head.right=x 
                    head=head.right
                return root
            
        