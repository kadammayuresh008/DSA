# https://leetcode.com/problems/kth-smallest-element-in-a-bst/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res=[]
        def inorder(self,root):
            if(root):
                inorder(self,root.left)
                res.append(root.val)
                inorder(self,root.right)
        inorder(self,root)
        return res[k-1]