# https://leetcode.com/problems/range-sum-of-bst/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum1=0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if(root==None):
            return self.sum1
        else:
            if(L<=root.val<=R):
                self.sum1+=root.val
            Solution.rangeSumBST(self,root.left,L,R)
            Solution.rangeSumBST(self,root.right,L,R)
            return self.sum1