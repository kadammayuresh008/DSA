
# https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum1(self,root):
        if(root==None):
            return 0
        return root.val+ Solution.sum1(self,root.right)+Solution.sum1(self,root.left)
    def findTilt(self, root: TreeNode) -> int:
        if(root):
            lh=Solution.sum1(self, root.left)
            rh=Solution.sum1(self, root.right)
            root.val=abs(lh-rh)
            if(root.left):
                Solution.findTilt(self, root.left)
            if(root.right):
                Solution.findTilt(self, root.right)
        return Solution.sum1(self, root)
        