# https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        lh=Solution.maxDepth(self,root.left)
        rh=Solution.maxDepth(self,root.right)
        return 1+max(lh,rh)
        