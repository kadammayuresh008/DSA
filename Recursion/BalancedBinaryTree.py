# https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def Height(self,root):
        if(root==None):
            return 0
        lh=Solution.Height(self,root.left)
        rh=Solution.Height(self,root.right)
        return 1+max(lh,rh)
    def isBalanced(self, root: TreeNode) -> bool:
        if(root==None):
            return True
        lh=Solution.Height(self,root.left)
        rh=Solution.Height(self,root.right)
        if(abs(rh-lh)>1):
            return False
        l=Solution.isBalanced(self, root.left)
        r=Solution.isBalanced(self, root.right)
        if l==True and r==True:
            return True