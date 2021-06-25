


# https://leetcode.com/problems/sum-root-to-leaf-numbers/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.sum1=0
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(self,root,s):
            if(root):
                s+=str(root.val)
                if(root.left==None and root.right==None):
                    self.sum1+=int(s)
                    dfs(self,root.left,s)
                if(root.left):
                    dfs(self,root.left,s)
                if(root.right):
                    dfs(self,root.right,s)
            return self.sum1
        x=dfs(self,root,"")
        return x
        